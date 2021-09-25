# Generate the key
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# key generation
key = get_random_bytes(32)

# iv generation
iv = AES.new(key, AES.MODE_CBC).iv

# Save the key to a file
file_out = open("TTP_key.bin", "wb")
file_out.write(key)
file_out.close()

# Save the iv to a file
file_out = open("TTP_iv.bin", "wb")
file_out.write(iv)
file_out.close()
