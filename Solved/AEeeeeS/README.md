# AEeeeeS
Cryptography

## Challenge 

... he encrypted the flag Using AES ECB.

the key he gave, is below.

Is he mad?

```ciphertext: c68145ccbc1bd6228da45a574ad9e29a77ca32376bc1f2a1e4cd66c640450d77```
Author: @mostwanted002


c68145ccbc1bd6228da45a574ad9e29a 77ca32376bc1f2a1e4cd66c640450d77

## Solution

In the key file, we see a binary string. 

If we convert it in any tool, we get gibberish.

But notice again there is 126 characters, which is not a multiple of 8.

We must pad 2 zeros to make it 128 characters or 16 bytes.

Got a bit lucky in decoding the binary using this function

	def bitstring_to_bytes(s):
	    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')
	 
And we can decipher it easily using PyCrypto

	 python3 solve.py 
	b'4*sqt(16)bytekey'
	b'encryptCTF{3Y3S_4R3_0N_A3S_3CB!}'

## Flag

	encryptCTF{3Y3S_4R3_0N_A3S_3CB!}
