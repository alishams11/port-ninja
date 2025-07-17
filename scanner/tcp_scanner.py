import socket

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
                    banner = s.recv(1024).decode().strip()
                    return (port, "open", banner if banner else None)
                except:
                    return (port, "open", None)
            else:
                return (port, "closed", None)
    except Exception as e:
        return (port, "error", str(e))
