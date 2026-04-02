import socket
import threading

HOST = "0.0.0.0"
PORT = 4444

def receive_messages(conn):
    while True:
        try:
            data = conn.recv(4096)
            if not data:
                print("[-] Client disconnected.")
                break
            print(f"\n[Client]: {data.decode()}\n[You]: ", end="", flush=True)
        except ConnectionResetError:
            print("[-] Connection closed by client.")
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[*] Listening on {HOST}:{PORT}...")
    conn, addr = s.accept()
    print(f"[+] Connected to {addr}!")

    
    threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()

    
    while True:
        msg = input("[You]: ")
        if msg.lower() in ("exit", "quit"):
            print("[*] Closing connection.")
            break
        conn.sendall(msg.encode())