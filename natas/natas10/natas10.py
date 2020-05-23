import base64
import json

default_cookie = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=".encode()
default_data = {"showpassword":"no","bgcolor":"#ffffff"}

def xor_encrypt(ciphertext,plaintext):
    key = ""
    for c1, c2 in zip(plaintext, ciphertext):
        key += chr(ord(c1) ^ ord(c2))
    # for i in range(len(ciphertext)):
    #     key += chr(ord(plaintext[i]) ^ ord(ciphertext[i % len(ciphertext)]))
    return key


## Input for xor should be base64 decoded
cookie_b64_decoded = (base64.b64decode(default_cookie)).decode()
xor_key = xor_encrypt(cookie_b64_decoded,json.dumps(default_data))
print(xor_key)
# print(json.dumps(default_data))
# obj = zip(default_cookie,json.dumps(default_data) )
# for c1,c2 in obj:
#     print(c1,c2)
# Idea is to use XOR weakness
# Data ^ Key = Cookie Data
# Cookie Data ^ Default Data = Key
