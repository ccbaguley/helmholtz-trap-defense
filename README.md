# Helmholtz Defense Framework

An advanced, multi-threaded behavioral cyber-defense daemon designed to trap, isolate, and exhaust anomalous network intrusion vectors silently.

## How It Works
Instead of traditional static antivirus scanning, this framework employs:
* **Orb Weaver Array:** A multi-threaded socket listener mapping real-world mobile vulnerability vectors (ADB `5555`, AirDrop `5353`, MDM `5223/8443`).
* **Helmholtz Resonance Chamber:** An isolated sandbox trap that catches incoming connection streams, answering them with high-speed looping synthetic decoy telemetry to exhaust the attacker's resources safely without throwing alerts.

---

## Installation & Deployment

### Step 1: Install Dependencies
Open your terminal and install the compiler configuration:
```bash
pip install pyinstaller
```

### Step 2: Compile the Binary
Compile the script into a background executable. Note that when deploying as a persistent system task, the standard binary path handles automation directly:
```bash
python -m PyInstaller --onefile --noconsole HelmholtzTrap.py
```

### Step 3: Configure Windows Firewall
Because the framework binds to specific connection ports, an inbound rule must be created to allow incoming network traffic to reach the daemon. Run this in an **Administrative PowerShell** window:
```powershell
New-NetFirewallRule -DisplayName "Helmholtz Honeypot Ports" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 5555, 5353, 5223, 8443
```

### Step 4: Configure Windows Task Scheduler
To ensure the binary runs permanently in the background with full system privileges:
1. Copy the compiled `HelmholtzTrap.exe` from your `.\dist` directory to a permanent system location, such as `C:\ProgramData\HelmholtzDefense\`.
2. Open **Task Scheduler** as an Administrator.
3. Click **Create Task** (not a Basic Task) and name it `HelmholtzTrap`.
4. Under **Security options**, change the user account to **`SYSTEM`** and check **Run with highest privileges**.
5. Set the **Trigger** to `At startup`.
6. Set the **Action** to `Start a program` and point it to `C:\ProgramData\HelmholtzDefense\HelmholtzTrap.exe`.

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
Test whether the Helmholtz Resonance Chamber is actively intercepting traffic and feeding synthetic data back to the initiator.

1. Open a PowerShell window and stream data from one of the configured ports using an interactive web request:
   ```powershell
   Invoke-WebRequest -Uri "http://127.0.0.1:5555" -MaximumRetryCount 0
   ```
2. While the request attempts to read the stream, open a separate terminal window to verify the socket state:
   ```cmd
   netstat -ano | findstr 5555
   ```
*Verification Check:* The connection list should display a row matching `127.0.0.1:5555` with the state marked as **`ESTABLISHED`** while the loop handles the socket. Alternatively, verify that a new entry appears in `C:\ProgramData\HelmholtzDefense\system_defense_daemon.log`.

---

## Troubleshooting & Common Deployment Errors

If you encounter initialization errors during compilation or task registration, look up the resolution matrix below.

### 1. PyInstaller Administrative Compilation Restriction
* **Symptoms:** 
  ```text
  DEPRECATION: Running PyInstaller as admin is not necessary nor sensible...
  ERROR: Do not run pyinstaller from C:\Windows\system32.
  ```
* **Cause:** PyInstaller explicitly blocks compilation tasks executed within administrative windows or core system paths to prevent accidental binary corruptions.
* **Resolution:** Close your elevated administrator window, open a standard user terminal instance, navigate cleanly to your repository folder workspace, and re-execute:
  ```powershell
  cd "$HOME\Documents\YourRepositoryPath"
  python -m PyInstaller --onefile --noconsole HelmholtzTrap.py
  ```

### 2. Task Scheduler Account Mapping Fault (HRESULT 0x80070534)
* **Symptoms:**
  ```text
  Register-ScheduledTask : No mapping between account names and security IDs was done.
  ```
* **Cause:** Your host environment is utilizing non-English, localized, or highly customized regional security strings, preventing Windows from correctly interpreting the default literal string `"NT AUTHORITY\SYSTEM"`.
* **Resolution:** Run the commands as a single inline block using the universal Security Identifier (SID) sequence for the root system profile, which remains constant across all international language environments (`S-1-5-18`):
  ```powershell
  \(Action = New-ScheduledTaskAction -Execute "C:\ProgramData\HelmholtzDefense\HelmholtzTrap.exe"; \)Trigger = New-ScheduledTaskTrigger -AtStartup; Register-ScheduledTask -TaskName "HelmholtzTrap" -Action Action -Trigger Trigger -User "S-1-5-18" -RunLevel Highest -Force
  ```

---

## Uninstallation Procedure

To completely remove the Helmholtz Defense Framework from the system, execute the following commands from an **Administrative PowerShell** window.

### Step 1: Remove the Windows Task Scheduler Task
Stop and delete the background system service task instantly without forcing an interactive prompt:
```powershell
Unregister-ScheduledTask -TaskName "HelmholtzTrap" -Confirm:0
```

### Step 2: Remove Windows Firewall Rules
Delete the custom inbound security rule created for the framework honey-pot ports:
```powershell
Remove-NetFirewallRule -DisplayName "Helmholtz Honeypot Ports"
```

### Step 3: Terminate Running Processes
If the daemon is currently executing inside the active memory space, kill the background binary process forcefully:
```powershell
Stop-Process -Name "HelmholtzTrap" -Force -ErrorAction SilentlyContinue
```

# Helmholtz Defense Framework

A multi-threaded behavioral network honeypot and resonance trap engineered to trap, identify, and exhaust anomalous network intrusion vectors.

## How It Works

- **HTTP Canary Web Trap:** A port listener (`Port 5353`) catching inbound browser connections from tracking tokens.
- **Helmholtz Resonance Chamber:** An isolated socket sandbox that loops synthetic decoy logs to exhaust attacker resources.
- **Unmasked Identification:** Captures true public IP addresses and User-Agent metrics natively.

## Installation & Deployment

1. **Firewall Rules:** Open inbound port `5353` via PowerShell.
2. **Launch Grid:** Initialize `HelmholtzTrap.py`.
3. **Embed Token:** Deploy a Google Apps Script Web App macro redirect pointing to your public IP and port.
4. **Verification:** Run `Get-NetTCPConnection` to confirm the listener is active on port `5353`.


### Step 4: Clean Up System Files
Delete the runtime application and log files safely from the storage directory:
```powershell
Remove-Item -Path "C:\ProgramData\HelmholtzDefense" -Recurse -Force -ErrorAction SilentlyContinue
```

## License
Distributed under the MIT License. See `LICENSE` for more information.
