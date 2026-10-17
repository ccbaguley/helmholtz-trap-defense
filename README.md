# Helmholtz Defense Framework

An advanced, multi-threaded behavioral cyber-defense daemon designed to trap, isolate, and exhaust anomalous network intrusion vectors silently. 

## How It Works
Instead of traditional static antivirus scanning, this framework employs:
* **Orb Weaver Array:** A multi-threaded socket listener mapping real-world mobile vulnerability vectors (ADB `5555`, AirDrop `5353`, MDM `5223/8443`).
* **Helmholtz Resonance Chamber:** An isolated sandbox trap that catches incoming connection streams, answering them with high-speed looping synthetic decoy telemetry to exhaust the attacker's resources safely without throwing alerts.

## Installation & Deployment
1. Install requirements: `pip install pyinstaller`
2. Compile into a cloaked background binary:
   ```bash
   python -m PyInstaller --onefile --noconsole --uac-admin HelmholtzTrap.py
   ```
3. Deploy the resulting executable from the `/dist` directory as a permanent background system service utilizing Windows Task Scheduler running with `SYSTEM` privileges.

## License
Distributed under the MIT License. See `LICENSE` for more information.
