# TopNOTCH_SA
Cryptography

## Challenge 


	(TopNOTCH)SA

	This admin's Obsession with RSA is beyond crazy, it's like he's being guided by some people more supreme, the top Notch of 7 Billion....

	Anyways, here's the archive, you know the deal. GodSpeed!

	Author:@mostwanted002



## Solution


	$ openssl rsa -inform PEM -pubin -in pubkey.pem -text -noout
	Public-Key: (255 bit)
	Modulus:
	    7f:fd:2b:1a:a7:27:47:f6:a0:1b:9f:96:77:78:7b:
	    a1:72:90:93:3e:3a:46:64:0c:ee:55:38:34:32:09:
	    ab:d1
	Exponent: 65537 (0x10001)

So

	n = 57891041571118599917733172578294383243762455810797917992757930072844611988433L
	e = 65537

Using factordb, it is already factorised

	p = 194038568404418855662295887732506969011
	q = 298348117320990514224871985940356407403

Solve using script
	
	$ python3 solve.py 
	b'encryptCTF{1%_0F_1%}\n'

## Flag

	encryptCTF{1%_0F_1%}
