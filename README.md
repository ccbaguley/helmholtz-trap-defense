# Helmholtz Defense Framework

An advanced, multi-threaded behavioral cyber-defense daemon designed to trap, isolate, and exhaust anomalous network intrusion vectors silently. 

## How It Works
Instead of traditional static antivirus scanning, this framework employs:
* **Orb Weaver Array:** A multi-threaded socket listener mapping real-world mobile vulnerability vectors (ADB `5555`, AirDrop `5353`, MDM `5223/8443`).
* **Helmholtz Resonance Chamber:** An isolated sandbox trap that catches incoming connection streams, answering them with high-speed looping synthetic decoy telemetry to exhaust the attacker's resources safely without throwing alerts.

## Installation & Deployment

### Step 1: Install Dependencies
Open your terminal and install the compiler configuration:
```bash
pip install pyinstaller
```

### Step 2: Compile the Binary
Compile the script into a cloaked background executable with administrative auto-elevation:
```bash
python -m PyInstaller --onefile --noconsole --uac-admin HelmholtzTrap.py
```

### Step 3: Configure Windows Task Scheduler
To ensure the binary runs permanently in the background with full system capabilities:
1. Open **Task Scheduler** as an Administrator.
2. Click **Create Task** (not a Basic Task) and name it `HelmholtzTrap`.
3. Under **Security options**, change the user account to **`SYSTEM`**.
4. Set the **Trigger** to `At startup`.
5. Set the **Action** to `Start a program` and point it to your compiled `HelmholtzTrap.exe` inside the `/dist` directory.

---

## Deployment Verification

Run the following validation steps from an **Administrative Command Prompt** or **PowerShell** to verify that the defense system is live.

### Step 1: Verify Active Network Listeners
Confirm that the daemon has successfully claimed and locked down the targeted honey-pot ports:

**Command Prompt:**
```cmd
netstat -ano | findstr /R "5555 5353 5223 8443"
```
**PowerShell:**
```powershell
Get-NetTCPConnection | Where-Object { \$_.LocalPort -in @(5555, 5353, 5223, 8443) }
```
*Verification Check:* Look for lines marked as **`LISTENING`**. Note the Process ID (PID) displayed at the far right.

### Step 2: Verify System Privilege Status
Ensure the process is actively executing under the protected system core context:

**Command Prompt:**
```cmd
tasklist /FI "IMAGENAME eq HelmholtzTrap.exe" /V
```
**PowerShell:**
```powershell
Get-Process -Name "HelmholtzTrap" | IncludeUserName
```
*Verification Check:* Confirm that the process is actively running and that the user context is explicitly set to **`NT AUTHORITY\SYSTEM`**.

### Step 3: Verify the Resonator Trap Functionality
Test whether the Helmholtz Resonance Chamber is actively intercepting attacks and exhausting remote system resources.

1. From a **separate machine** or local WSL instance on the same network, attempt an explicit connection to one of your listening ports (e.g., port 5555):
   ```bash
   nc -v <TARGET_HOST_IP> 5555
   ```
2. While that connection is active, return to your **Administrative terminal** on the host machine and run:
   ```cmd
   netstat -ano | findstr /R "5555 5353 5223 8443"
   ```

*Verification Check:* You should now see an active connection row marked as **`ESTABLISHED`**. The trap will hold this connection open indefinitely, quietly flooding the remote target with loop telemetry to deplete their socket capacity.

---

## License
Distributed under the MIT License. See `LICENSE` for more information.
