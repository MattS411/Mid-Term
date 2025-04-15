# port_scanner.py
import socket
from datetime import datetime

target = input("Enter host (127.0.0.1 or scanme.nmap.org): ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\n[+] Scanning {target} from port {start_port} to {end_port}")
print("Scan started:", datetime.now())

try:
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"[OPEN] Port {port}")
        s.close()
except socket.gaierror:
    print("[!] Invalid hostname.")
except socket.error:
    print("[!] Could not connect to target.")
except ValueError:
    print("[!] Invalid port number.")

print("Scan completed:", datetime.now())
print("[!] Port scanning finished.")
# This code is a simple port scanner that checks for open ports on a specified host.    