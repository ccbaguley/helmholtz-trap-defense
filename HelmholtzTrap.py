import os
import sys
import time
import random
import logging
import socket
import threading
from logging.handlers import RotatingFileHandler

# 1. Establish persistent, global system directory paths for service data
LOG_DIRECTORY = r"C:\ProgramData\HelmholtzDefense"
LOG_FILE_PATH = os.path.join(LOG_DIRECTORY, "system_defense_daemon.log")

# Automatically generate the secure storage vault folder if the system lacks it
if not os.path.exists(LOG_DIRECTORY):
    try:
        os.makedirs(LOG_DIRECTORY)
    except Exception as e:
        sys.exit(f"Critical Error: Failed to create logging directory: {e}")

# SAFE GUARDRAIL: Use a RotatingFileHandler to cap log files at 5MB, keeping a maximum of 3 logs
log_handler = RotatingFileHandler(LOG_FILE_PATH, maxBytes=5 * 1024 * 1024, backupCount=3)
logging.basicConfig(
    handlers=[log_handler],
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] (%(threadName)s) %(message)s'
)

class HelmholtzCanaryTrap:
    def _generate_synthetic_telemetry(self):
        """Generates continuous fake telemetry to safely exhaust the active connection."""
        while True:
            # Synthetic decoy tracking telemetry mimicking regional coordinates
            mock_lat = random.uniform(-6.2088, -6.3000)
            mock_lon = random.uniform(106.8456, 106.9000)
            yield f'{{"gps": "{mock_lat}, {mock_lon}", "status": "ACK"}}\n'

    def neutralize_threat(self, port_vector, client_socket, client_address):
        """The Resonance Chamber: Safely exhausts the incoming connection using low-level socket streams."""
        logging.warning(f"[RESONATOR] Inbound anomaly quarantined from {client_address} on Web Strand (Port {port_vector}).")
        
        decoy_stream = self._generate_synthetic_telemetry()
        client_socket.settimeout(1.0) # Prevent the client thread from hanging forever
        
        try:
            # Safe absorption loops to stress-test attacker allocations
            for _ in range(50):
                poisoned_payload = next(decoy_stream)
                # Send the synthetic decoy payload directly back through the open socket connection
                client_socket.sendall(poisoned_payload.encode('utf-8'))
                time.sleep(0.05) # Rate-limited throttling cycle to balance memory footprints
        except (socket.error, socket.timeout):
            # Gracefully handle situations where the remote attacker drops or disconnects
            pass
        finally:
            try:
                client_socket.shutdown(socket.SHUT_RDWR)
                client_socket.close()
            except socket.error:
                pass
            logging.info(f"[RESONATOR] Threat vector from {client_address} on Port {port_vector} safely collapsed.")

class OrbWeaverWeb:
    def __init__(self, trap_handler):
        self.trap = trap_handler
        # SAFE GUARDRAIL: Limit concurrent active traps to 10 to guarantee 0% CPU lockups under load
        self.thread_pool_semaphore = threading.Semaphore(10)
        
        # Real-world mobile vulnerability configuration matrix
        self.web_strands = [
            5555,  # Android Debug Bridge (ADB over Wi-Fi)
            5353,  # Apple mDNS / AirDrop Discovery Vector
            8770,  # iOS Local Wireless Services
            5223,  # Apple Push Notification Service (APNS / MDM Profiles)
            8443,  # Mobile Device Management (MDM Integration)
            8080   # Alternative Web Proxy (Data Exfiltration Vector)
        ]
        self.is_spinning = True

    def spin_strand(self, port):
        """Monitors a specific network port using non-blocking raw socket bindings."""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Prevent socket port lockups on restart
        server.settimeout(2.0) # Avoid infinite thread blocking states
        
        try:
            # Bind to all network interfaces locally to act as a proper honeypot net
            server.bind(('0.0.0.0', port))
            server.listen(128)
            logging.info(f"[ORB WEAVER] Real socket web strand secured and listening on Port {port}...")
        except Exception as e:
            logging.error(f"[CRITICAL] Web strand failed to bind to Port {port}: {e}")
            return

        while self.is_spinning:
            try:
                client_sock, client_addr = server.accept()
                logging.warning(f"[ORB WEAVER] Inbound vibration caught on Port {port} from source {client_addr}!")
                
                # Check the semaphore limits to see if we have available thread slots
                if self.thread_pool_semaphore.acquire(blocking=False):
                    action_thread = threading.Thread(
                        target=self._managed_neutralization, 
                        args=(port, client_sock, client_addr),
                        name=f"ResonatorPool-Port{port}"
                    )
                    action_thread.daemon = True
                    action_thread.start()
                else:
                    logging.error(f"[RESOURCE LIMIT] Max traps reached! Dropping packet context instantly from {client_addr}.")
                    client_sock.close()
                    
            except socket.timeout:
                continue
            except Exception as e:
                logging.error(f"[ERROR] Socket acceptance fault encountered on Port {port}: {e}")
                break
                
        server.close()

    def _managed_neutralization(self, port, client_sock, client_addr):
        """Wraps the threat runtime within the semaphore bounds to enforce resource throttling."""
        try:
            self.trap.neutralize_threat(port, client_sock, client_addr)
        finally:
            self.thread_pool_semaphore.release() # Open up a slot for the next incoming attack

    def deploy_web(self):
        """Launches all mobile vulnerability web strands simultaneously in parallel background threads."""
        for strand in self.web_strands:
            thread = threading.Thread(target=self.spin_strand, args=(strand,), name=f"OrbWeaverStrand-{strand}")
            thread.daemon = True
            thread.start()

def run_daemon_loop():
    """Main execution orchestrator initializing components and keeping the core service alive."""
    resonator_trap = HelmholtzCanaryTrap()
    spider_web = OrbWeaverWeb(resonator_trap)
    
    # Deploy the parallel raw socket array
    spider_web.deploy_web()
    
    logging.info("System Defense Daemon fully operational, safe, and deployed.")
    
    # Keep master execution thread alive silently
    while True:
        try:
            time.sleep(1.0)
        except KeyboardInterrupt:
            logging.info("Background service terminated by administrator via manual interrupt command.")
            spider_web.is_spinning = False
            sys.exit(0)

# --- EXECUTE ARCHITECTURAL RUNTIME ---
if __name__ == "__main__":
    # Adjust this runtime path to match your local Python Scripts installation directory
    sys.path.append(r"C:\Users\YOUR_USERNAME\AppData\Local\Python\Python314\Scripts")
    
    # Trigger the background service daemon
    run_daemon_loop()
