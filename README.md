# [+] CyberSec Toolkit

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.txt)

A modular cybersecurity framework for network analysis and penetration testing with military-grade encryption and advanced monitoring capabilities.

## [+] Features

- **NSA-Grade Authentication System** 🔑
  - BCrypt password hashing
  - Port security verification
  - IP whitelisting
- **WiFi Warfare Suite** 📡
  - Network topology mapping
  - Connected device fingerprinting
  - Encryption vulnerability detection
- **Dark Matrix Device Scanner** 💀
  - MAC address vendor identification
  - Port vulnerability assessment
  - CVE database integration
- **ZeroTrace Logging System** 📜
  - AES-256 encrypted activity logs
  - Network state snapshots
  - Forensic-ready audit trails

## [+] Installation

**Requirements:**
- Python 3.8+
- Linux kernel 4.4+ (recommended)
- Wireless interface in monitor mode

```bash
# Clone with paranoid mode
git clone https://github.com/Kennny7/CyberSec-Toolkit.git --config core.hooksPath=.githooks

cd CyberSec-Toolkit

# Install requirements (use virtualenv)
pip install -r requirements.txt

# Install system dependencies
sudo apt install arp-scan nmap wireless-tools
```

## [+] Usage

```bash
python main.py
```

**Sample Workflow:**
1. Enter master password: *********
2. Select module: `WiFi Analysis`
3. Select interface: `wlan0`
4. Choose scan type: `Deep Packet Inspection`
5. Review identified vulnerabilities

![Terminal Demo](docs/demo.gif)

## [+] Project Structure

```
CyberSec-Toolkit/
├── main.py                 - Main entry point
├── auth/                   - Security subsystem
│   ├── security.py         - Authentication core
│   └── vault.py            - Credential storage
├── modules/                - Hacking modules
│   ├── wifi_warrior/       - Wireless suite
│   │   ├── sniffer.py      - Packet analysis
│   │   └── deauth.py       - AP communication
│   └── dark_scanner/       - Host enumeration
├── utilities/              - Support systems
│   ├── crypto.py           - AES/RSA operations
│   ├── logger.py           - Forensic logging
│   └── syscheck.py         - Environment verification
├── config/                 - Configuration
│   ├── cve_db.json         - Vulnerability database
│   └── signatures/         - Device fingerprints
├── requirements.txt        - Python dependencies
└── .gitignore              - Security exclusions
```

## [+] Cyber Ethics Disclaimer

This tool is strictly for:
- Authorized penetration testing
- Cybersecurity education
- Network defense research

**Warning:** Unauthorized access to computer systems violates:
- Computer Fraud and Abuse Act (CFAA)
- EU GDPR Article 32
- UK Computer Misuse Act

## [+] Contributing

Paranoid development protocol:
1. GPG-sign all commits
2. Use `git commit --verify-signatures`
3. Submit to TOR-hidden repository mirror
4. Wait for 3 maintainer confirmations

## [+] License

GNU General Public License v3.0 - See [LICENSE](LICENSE) for full text

