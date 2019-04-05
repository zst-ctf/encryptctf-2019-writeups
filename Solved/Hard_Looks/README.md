# Hard Looks
Cryptography

## Challenge 

Does this look hard?

	CipherText: --_--___--_-_-__--_--__--__-_-__--_--___--__--__--_---__--__-___--_---__---__-__--_---__--______--_---__--_-____--_-____--__--__--_-_-__--_-____--_-____--_--___--_---_--___-___--_-_-__--_---__--__--__--_-____--__--__--_-_-__--_-_-_--__--___--__--__--___-__--__--__--_---__--_-_-_--__--___--_-____---_____--__--__--_-____--_-_-__--__-___--_-____--_-____--_-_-_--__--___--__--__--__--__--_-___--__-_-__--__--__--______--_-_-__--_-_-__--_-____--_---__--_-____---_____--__--_--__--___--__-___--___-__--_---_--__-__

	Author: @mostwanted002

## Solution

Looks like binary because of "high" and "low"

	$ cat ciphertext.txt | perl -pe 's/-/1/g' | perl -pe 's/_/0/g'
	110110001101010011011001100101001101100011001100110111001100100011011100111001001101110011000000110111001101000011010000110011001101010011010000110100001101100011011101100010001101010011011100110011001101000011001100110101001101010110011000110011001100010011001100110111001101010110011000110100001110000011001100110100001101010011001000110100001101000011010101100110001100110011001100110100011001010011001100110000001101010011010100110100001101110011010000111000001100110110011000110010001100010011011101100100

There are 510 chars, which rounds up to 512 bits or 64 bytes

So prepend 2 zeros to form complete binary

	00110110001101010011011001100101001101100011001100110111001100100011011100111001001101110011000000110111001101000011010000110011001101010011010000110100001101100011011101100010001101010011011100110011001101000011001100110101001101010110011000110011001100010011001100110111001101010110011000110100001110000011001100110100001101010011001000110100001101000011010101100110001100110011001100110100011001010011001100110000001101010011010100110100001101110011010000111000001100110110011000110010001100010011011101100100

Then convert to ascii

	656e63727970744354467b5734355f31375f483452445f334e305547483f217d

it gives us a hex string, so convert it again

	$ echo xx | perl -lpe '$_=pack"B*",$_' | xxd -r -p
	encryptCTF{W45_17_H4RD_3N0UGH?!}

## Flag

	encryptCTF{W45_17_H4RD_3N0UGH?!}