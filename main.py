import json  
from datetime import datetime  
from scanner.tcp_scanner import threaded_scan
from scanner.udp_scanner import udp_scan

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
    print("=== Port Ninja Scanner ===")
    host = input("Enter target IP or domain: ").strip()
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))
    
    scan_type = input("Scan type (tcp / udp): ").strip().lower()

    ports = range(start_port, end_port + 1)

    open_tcp = []
    open_udp = []

    if scan_type == "tcp":
        print(f"\n[*] TCP Scan on {host} from port {start_port} to {end_port}...\n")
        results = threaded_scan(host, ports)

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

    elif scan_type == "udp":
        print(f"\n[*] UDP Scan on {host} from port {start_port} to {end_port}...\n")
        for port in ports:
            is_open, response = udp_scan(host, port)
            if is_open:
                open_udp.append(port) 
                print(f"[+] UDP Port {port} is OPEN", end="")
                if response:
                    print(f" | Response: {response}")
                else:
                    print()
        print("\n[!] Note: UDP scans may not always be reliable due to lack of response.")

    else:
        print("[!] Invalid scan type. Please enter 'tcp' or 'udp'.")
        return

    save_results(host, open_tcp, open_udp)

if __name__ == "__main__":
    main()
