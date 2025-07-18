from scanner.tcp_scanner import threaded_scan
def main():
    print("=== Port Ninja TCP Scanner ===")
    host = input("Enter target IP or domain: ").strip()
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))
    ports = range(start_port, end_port + 1)


    print(f"\n[*] Scanning {host} from port {start_port} to {end_port}...\n")
    results = threaded_scan(host, ports)
    
    if results:
        print("[+] Open ports:")
        for port, banner in results:
            print(f"    - Port {port} is OPEN", end="")
            if banner:
                print(f" | Banner: {banner}")
            else:
                print()
    else:
        print("[-] No open ports found.")
        
if __name__ == "__main__":
    main()
