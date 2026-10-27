import os
import sys
import time
import random
import logging
import socket
import threading
from pathlib import Path
from logging.handlers import RotatingFileHandler

# Define cross-platform production storage and logging fallback directories
if os.name == 'nt':
    LOG_DIRECTORY = Path(os.environ.get("PROGRAMDATA", r"C:\ProgramData")) / "HelmholtzDefense"
else:
    LOG_DIRECTORY = Path("/var/log/helmholtzdefense")

LOG_FILE_PATH = LOG_DIRECTORY / "system_defense_daemon.log"

# Automatically generate system folders with safe permissions
if not LOG_DIRECTORY.exists():
    try:
        LOG_DIRECTORY.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        sys.exit(f"Critical Initialization Failure: Cannot create logging structure: {e}")

# Secure log rotation parameters (Capped at 5MB, maintaining 3 history fragments)
log_handler = RotatingFileHandler(str(LOG_FILE_PATH), maxBytes=5 * 1024 * 1024, backupCount=3)
logging.basicConfig(
    handlers=[log_handler],
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] (%(threadName)s) %(message)s'
)

class HelmholtzCanaryTrap:
    def _generate_synthetic_telemetry(self):
        """Generates continuous fake telemetry to safely exhaust the active connection."""
        while True:
            mock_lat = random.uniform(-6.2088, -6.3000)
            mock_lon = random.uniform(106.8456, 106.9000)
            yield f'{{"gps": "{mock_lat}, {mock_lon}", "status": "ACK"}}\n'

    def neutralize_threat(self, port_vector, client_socket, client_address):
        """The Resonance Chamber: Safely exhausts the incoming connection using low-level socket streams."""
        logging.warning(f"[RESONATOR] Inbound anomaly quarantined from {client_address} on Port {port_vector}.")
        
        decoy_stream = self._generate_synthetic_telemetry()
        client_socket.settimeout(1.0)  # Defensive timeout baseline to prevent thread stalling
        
        try:
            for _ in range(50):
                poisoned_payload = next(decoy_stream)
                client_socket.sendall(poisoned_payload.encode('utf-8'))
                time.sleep(0.05)  # Rate-limited pacing interval
        except (socket.error, socket.timeout):
            pass
        finally:
            try:
                client_socket.shutdown(socket.SHUT_RDWR)
                client_socket.close()
            except socket.error:
                pass
            logging.info(f"[RESONATOR] Threat vector from {client_address} on Port {port_vector} safely collapsed.")

class OrbWeaverWeb:
    def __init__(self, trap_handler, monitored_ports=None):
        self.trap = trap_handler
        # Thread constraints to cap operational footprint under heavy traffic
        self.thread_pool_semaphore = threading.Semaphore(10)
        
        # Configurable port list with default security targets if unspecified
        self.web_strands = monitored_ports or [5555, 5353, 8770, 5223, 8443, 8080]
        self.is_spinning = True

    def spin_strand(self, port):
        """Monitors a specific network port using non-blocking raw socket bindings."""
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.settimeout(2.0)
        
        try:
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
                
                if self.thread_pool_semaphore.acquire(blocking=False):
                    action_thread = threading.Thread(
                        target=self._managed_neutralization, 
                        args=(port, client_sock, client_addr),
                        name=f"ResonatorPool-Port{port}"
                    )
                    action_thread.daemon = True
                    action_thread.start()
                else:
                    logging.error(f"[RESOURCE LIMIT] Max traps reached! Dropping context from {client_addr}.")
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
            self.thread_pool_semaphore.release()

    def deploy_web(self):
        """Launches all mobile vulnerability web strands simultaneously in parallel background threads."""
        for strand in self.web_strands:
            thread = threading.Thread(target=self.spin_strand, args=(strand,), name=f"OrbWeaverStrand-{strand}")
            thread.daemon = True
            thread.start()

def run_daemon_loop():
    """Main execution orchestrator keeping the core network components running cleanly."""
    resonator_trap = HelmholtzCanaryTrap()
    spider_web = OrbWeaverWeb(resonator_trap)
    spider_web.deploy_web()
    
    logging.info("System Defense Daemon fully operational, safe, and deployed.")
    
    while True:
        try:
            time.sleep(1.0)
        except KeyboardInterrupt:
            logging.info("Background service terminated by administrator via manual interrupt command.")
            spider_web.is_spinning = False
            sys.exit(0)

if __name__ == "__main__":
    run_daemon_loop()
