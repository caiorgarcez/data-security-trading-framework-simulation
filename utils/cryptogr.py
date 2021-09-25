from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

with open("TTP_key.bin", 'rb') as input_file:
    
# Later on ... (assume we no longer have the key)
file_in = open(, "rb") # Read bytes
key_from_file = file_in.read() # This key should be the same
iv = file_in.read(16)
file_in.close()

import ipdb

ipdb.set_trace()
# # TODO: change to a context manager
# file_in = open("TTP_key.bin", "rb") # Read bytes
# key_from_file = file_in.read() # This key should be the same
# file_in.close() 


# cipher = AES.new(key_from_file, AES.MODE_CBC)

# data = b"oi galera!"

# ciphered_data = cipher.encrypt(pad(data, AES.block_size)) # Pad the input data and then encrypt

# # original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) # Decrypt and then up-pad the result

# print(f"key: {key_from_file} \n message: {data} \n encrypted: {ciphered_data}") # \n decrypted: {original_data}")
