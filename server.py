# server.py
import socket

HOST = '127.0.0.1'
PORT = 65432

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[+] Server listening on {HOST}:{PORT}")

    conn, addr = server.accept()
    print(f"[+] Connected by {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"[Client]: {data}")
        conn.sendall(f"Server received: {data}".encode())

    conn.close()
    server.close()
except Exception as e:
    print(f"[!] Error: {e}")
except KeyboardInterrupt:
    print("\n[!] Server shutting down...")  