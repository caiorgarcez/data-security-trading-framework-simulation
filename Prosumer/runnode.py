import socket

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

HEADER = 64
PORT = 65432
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.1.2"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

file_in = open("TTP_key.bin", "rb")  # Read bytes
key_from_file = file_in.read()  # This key should be the same
file_in.close()

file_in = open("TTP_iv.bin", "rb")  # Read bytes
iv = file_in.read()  # This key should be the same
file_in.close()

# setup cipher
cipher = AES.new(key_from_file, AES.MODE_CBC, iv=iv)


def send(msg):
    message = msg
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


ciphered_data = cipher.encrypt(pad(b"Ciphered hello", AES.block_size))
send(ciphered_data)
input()
ciphered_data = cipher.encrypt(pad(b"Ciphered hello two", AES.block_size))
send(ciphered_data)
input()
ciphered_data = cipher.encrypt(pad(b"Ciphered hello threeeeeeee", AES.block_size))
send(ciphered_data)

send(DISCONNECT_MESSAGE)

# #!/usr/bin/env python3

# import socket

# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# from Crypto.Util.Padding import pad, unpad

# HOST = '192.168.1.2'  # The server's hostname or IP address
# PORT = 65432

# # TODO: change to a context manager
# file_in = open("TTP_key.bin", "rb") # Read bytes
# key_from_file = file_in.read() # This key should be the same
# file_in.close()     # The port used by the server

# file_in = open("TTP_iv.bin", "rb") # Read bytes
# iv = file_in.read() # This key should be the same
# file_in.close()

# # setup cipher
# cipher = AES.new(key_from_file, AES.MODE_CBC, iv=iv)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     data = b"oi galera!"
#     ciphered_data = cipher.encrypt(pad(data, AES.block_size))
#     s.connect((HOST, PORT))
#     s.sendall(ciphered_data)
#     data = s.recv(1024)

# print('Received', repr(data))
