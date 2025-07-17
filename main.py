from scanner.tcp_scanner import scan_port

def main():
    print("=== Port Ninja TCP Scanner ===")
    host = input("Enter target IP or domain: ").strip()
    start_port = int(input("Start port: "))
    end_port = int(input("End port: "))

    for port in range(start_port, end_port + 1):
        port, status, banner = scan_port(host, port)
        if status == "open":
            print(f"[+] Port {port} is OPEN", end="")
            if banner:
                print(f" | Banner: {banner}")
            else:
                print()
        elif status == "closed":
            print(f"[-] Port {port} is closed")
        else:
            print(f"[!] Error scanning port {port}: {banner}")
