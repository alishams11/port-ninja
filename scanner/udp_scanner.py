import socket

def udp_scan(host, port, timeout=2):
    """
    Perform a basic UDP scan on the target host and port.
    Returns True if there's a response (port likely open),
    or False if no response (may be filtered or closed).
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(timeout)

        # Send dummy packet (can be empty or a known payload)
        sock.sendto(b"\x00", (host, port))

        # Try to receive a response
        data, _ = sock.recvfrom(1024)
        return True, data.decode(errors="ignore") if data else None

    except socket.timeout:
        return False, None  # No response, possibly filtered/closed
    except Exception:
        return False, None
    finally:
        sock.close()
