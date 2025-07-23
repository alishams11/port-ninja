# 🥷 Port Ninja - Stealthy Port Scanner

**Port Ninja** is a fast and simple CLI-based port scanner for security testers and penetration testers. It supports both **TCP** and **UDP** scans with optional banner grabbing, multithreading, and clean JSON output reports.

---

## 🚀 Features

- 🔍 TCP port scanning with optional banner grabbing  
- 🛰️ UDP port scanning (basic response check)  
- ⚡ Fast multithreaded scanning  
- 📁 Outputs results in structured `JSON`  
- 🎯 CLI interface with `argparse` for automation  
- 🧪 Tested on `localhost` and real environments

---

## 📦 Installation

```bash
git clone https://github.com/<your-username>/port-ninja.git
cd port-ninja
pip install -r requirements.txt


#🛠 Usage

python3 main.py -t <target> --tcp --udp --ports <start>-<end>

#✅ Examples

# TCP scan from ports 20 to 100
python3 main.py -t 127.0.0.1 --tcp --ports 20-100

# UDP scan only
python3 main.py -t example.com --udp --ports 50-60

# Combined TCP & UDP scan
python3 main.py -t 192.168.1.1 --tcp --udp --ports 1-1024

#📁 Output Format

The scan result is saved to outputs/results.json like this:

{
  "target": "127.0.0.1",
  "open_ports": {
    "tcp": [22, 80],
    "udp": [53]
  },
  "timestamp": "2025-07-23 15:00"
}

#📸 Screenshot

CLI Demo
#🧱 Project Structure

port-ninja/
├── scanner/
│   ├── tcp_scanner.py
│   └── udp_scanner.py
├── outputs/
│   └── results.json
├── screenshots/
│   └── demo.png
├── main.py
├── requirements.txt
├── LICENSE
└── README.md


