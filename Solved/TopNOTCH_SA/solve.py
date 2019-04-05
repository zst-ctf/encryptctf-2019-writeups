#!/usr/bin/env python3
from Crypto.Util.number import *
import gmpy2

p = 194038568404418855662295887732506969011
q = 298348117320990514224871985940356407403
n = 57891041571118599917733172578294383243762455810797917992757930072844611988433

assert (n == p*q)

e = 65537
phi = (p-1)*(q-1)
d = gmpy2.invert(e,phi)

ciphertext = '369ad6199548d8181c26d112d1061008c056f08c75339366435046a9a8fbf295'
ciphertext = bytes.fromhex(ciphertext)
ciphertext = bytes_to_long(ciphertext)

plaintext = pow(ciphertext, d, n)
print(bytes.fromhex("%x" % plaintext))
