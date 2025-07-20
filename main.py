from scanner.tcp_scanner import threaded_scan
from scanner.udp_scanner import udp_scan

def main():
    print("=== Port Ninja Scanner ===")
    host = input("Enter target IP or domain: ").strip()
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))
    scan_type = input("Scan type (tcp / udp): ").strip().lower()

    ports = range(start_port, end_port + 1)

    if scan_type == "tcp":
        print(f"\n[*] TCP Scan on {host} from port {start_port} to {end_port}...\n")
        results = threaded_scan(host, ports)

        if results:
            print("[+] Open TCP ports:")
            for port, banner in results:
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
            open_udp, response = udp_scan(host, port)
            if open_udp:
                print(f"[+] UDP Port {port} is OPEN", end="")
                if response:
                    print(f" | Response: {response}")
                else:
                    print()
        print("\n[!] Note: UDP scans may not always be reliable due to lack of response.")

    else:
        print("[!] Invalid scan type. Please enter 'tcp' or 'udp'.")

if __name__ == "__main__":
    main()
