import argparse
import json
from datetime import datetime
from scanner.tcp_scanner import threaded_scan
from scanner.udp_scanner import udp_scan


def parse_ports(port_range):
    try:
        start, end = map(int, port_range.split("-"))
        return range(start, end + 1)
    except Exception:
        raise argparse.ArgumentTypeError("Invalid port range. Use format like 20-100")


def save_results(target, tcp_ports, udp_ports):
    data = {
        "target": target,
        "open_ports": {
            "tcp": tcp_ports,
            "udp": udp_ports
        },
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    try:
        with open("outputs/results.json", "w") as f:
            json.dump(data, f, indent=4)
        print(f"\n[+] Results saved to outputs/results.json")
    except Exception as e:
        print(f"[!] Failed to save results: {e}")


def main():
    parser = argparse.ArgumentParser(description="🛡️ Port Ninja - Fast TCP/UDP Port Scanner")
    parser.add_argument("-t", "--target", required=True, help="Target IP or domain")
    parser.add_argument("--tcp", action="store_true", help="Enable TCP scan")
    parser.add_argument("--udp", action="store_true", help="Enable UDP scan")
    parser.add_argument("--ports", type=parse_ports, default=range(1, 1025),
                        help="Port range (e.g., 1-1000)")

    args = parser.parse_args()

    target = args.target
    ports = args.ports

    open_tcp = []
    open_udp = []

    if not args.tcp and not args.udp:
        print("[!] No scan type selected. Use --tcp and/or --udp.")
        return

    if args.tcp:
        print(f"\n[*] Starting TCP scan on {target}...\n")
        results = threaded_scan(target, ports)
        if results:
            print("[+] Open TCP ports:")
            for port, banner in results:
                open_tcp.append(port)
                print(f"    - Port {port} is OPEN", end="")
                if banner:
                    print(f" | Banner: {banner}")
                else:
                    print()
        else:
            print("[-] No open TCP ports found.")

    if args.udp:
        print(f"\n[*] Starting UDP scan on {target}...\n")
        for port in ports:
            is_open, response = udp_scan(target, port)
            if is_open:
                open_udp.append(port)
                print(f"    - UDP Port {port} is OPEN", end="")
                if response:
                    print(f" | Response: {response}")
                else:
                    print()
        print("\n[!] Note: UDP scans may not always be reliable due to lack of response.")

    save_results(target, open_tcp, open_udp)


if __name__ == "__main__":
    main()
