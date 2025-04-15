import socket

HOST = '127.0.0.1'
PORT = 65432

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[DEBUG] Trying to connect...")
    client.connect((HOST, PORT))
    print("[+] Connected to server")

    message = input("Enter message: ")
    print("[DEBUG] Sending message...")
    client.sendall(message.encode())

    print("[DEBUG] Waiting for response...")
    response = client.recv(1024).decode()
    print(f"[Server]: {response}")

    client.close()
except ConnectionRefusedError:
    print("[!] Server is not running.")
except Exception as e:
    print(f"[!] Error: {e}")
except KeyboardInterrupt:
    print("\n[!] Client shutting down...")  