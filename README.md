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

### Step 3: Configure Windows Firewall
Because the framework binds to specific connection ports, an inbound rule must be created to allow incoming network traffic to reach the daemon. Run this in an **Administrative PowerShell** window:
```powershell
New-NetFirewallRule -DisplayName "Helmholtz Honeypot Ports" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 5555, 5353, 5223, 8443
```

### Step 4: Configure Windows Task Scheduler
To ensure the binary runs permanently in the background with full system capabilities:
1. Open **Task Scheduler** as an Administrator.
2. Click **Create Task** (not a Basic Task) and name it `HelmholtzTrap`.
3. Under **Security options**, change the user account to **`SYSTEM`**.
4. Set the **Trigger** to `At startup`.
5. Set the **Action** to `Start a program` and point it to your compiled `HelmholtzTrap.exe` inside the `/dist` directory.

---

## Deployment Verification

Run the following validation steps from your Command Prompt or PowerShell to verify that the defense system is live.

### Step 1: Verify Active Network Listeners
Confirm that the daemon has successfully claimed and locked down the targeted honey-pot ports:

**Command Prompt:**
```cmd
netstat -ano | findstr /R "5555 5353 5223 8443"
```

**PowerShell:**
```powershell
Get-NetTCPConnection | Where-Object LocalPort -in 5555, 5353, 5223, 8443
```
*Verification Check:* Look for lines marked as **`LISTENING`**. Note the Process ID (PID) displayed at the far right.

### Step 2: Verify Background Process Status
Confirm that the binary is actively running in the background:

**Command Prompt:**
```cmd
tasklist /FI "IMAGENAME eq HelmholtzTrap.exe" /V
```

**PowerShell:**
```powershell
Get-Process -Name "HelmholtzTrap"
```
*Verification Check:* Confirm that the process is actively listed with its unique ID (PID).

### Step 3: Verify the Resonator Trap Functionality (Local Loopback Test)
Test whether the Helmholtz Resonance Chamber is actively intercepting traffic and holding connection channels locally.

1. Open a PowerShell window and test the connection locally against the loopback adapter:
   ```powershell
   Test-NetConnection -ComputerName 127.0.0.1 -Port 5555
   ```
2. While that connection command is running or immediately after, open a separate terminal window and check the connection socket states:
   ```cmd
   netstat -ano | findstr /R "5555 5353 5223 8443"
   ```

*Verification Check:* The connection test should return **`TcpTestSucceeded : True`**. In your network listener list, you should see an active connection row marked as **`ESTABLISHED`** showing `127.0.0.1:5555`. The trap will hold this socket open indefinitely.

---

## License
Distributed under the MIT License. See `LICENSE` for more information.
