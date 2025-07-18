import socket
import threading

open_ports = []

def scan_port(host, port, timeout=1):
    """
    Attempts to connect to a TCP port and return status and optional banner.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            if result == 0:
                try:
                    banner = s.recv(1024).decode(errors="ignore").strip()
                    open_ports.append((port, banner if banner else None))
                except:
                    open_ports.append((port, None))
    except:
        pass  

def threaded_scan(host, ports, threads=100):
    
    thread_list = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(host, port))
        thread_list.append(t)
        t.start()

        if len(thread_list) >= threads:
            for thread in thread_list:
                thread.join()
            thread_list = []

    for thread in thread_list:
        thread.join()

    return open_ports
