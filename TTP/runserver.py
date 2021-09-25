import socket
import threading

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

HEADER = 64
PORT = 65432
SERVER = "192.168.1.2"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

file_in = open("TTP_key.bin", "rb")  # Read bytes
key_from_file = file_in.read()  # This key should be the same
file_in.close()

file_in = open("TTP_iv.bin", "rb")  # Read bytes
iv = file_in.read()  # This key should be the same
file_in.close()

# setup cipher
cipher = AES.new(key_from_file, AES.MODE_CBC, iv=iv)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length)
            original_data = unpad(cipher.decrypt(msg), AES.block_size)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {original_data}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()


# import socket


# HOST =   # Standard loopback interface address (localhost)
# PORT = 65432  # Port to listen on (non-privileged ports are > 1023)


# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     conn, addr = s.accept()
#     with conn:
#         print("Connected by", addr)
#         while True:
#             data = conn.recv(1024)
#             print(f"received data: {data} \n decryped data: {original_data}")
#             if not data:
#                 break
#             conn.sendall(original_data)
