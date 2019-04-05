from Crypto.Cipher import AES

import binascii

def bitstring_to_bytes(s):
	return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

with open("AEeeeeS.key", "r") as f:
	key = f.read().strip()
	key = bitstring_to_bytes(key)
	print(key)

ct = 'c68145ccbc1bd6228da45a574ad9e29a77ca32376bc1f2a1e4cd66c640450d77'
ct = bytes.fromhex(ct)
decipher = AES.new(key, AES.MODE_ECB)
print(decipher.decrypt(ct))
