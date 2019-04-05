from itertools import cycle
import string

x = b''
x += (0x2e191d141f0e0308).to_bytes(8, byteorder='little')
x += (0x1f020a012c162b39).to_bytes(8, byteorder='little')
x += (0x203401e00051904).to_bytes(8, byteorder='little')
x += (0xc084019).to_bytes(4, byteorder='little')
x += (0x141e).to_bytes(2, byteorder='little')
x += (0x10).to_bytes(1, byteorder='little')


def bxor(a1, b1):
    encrypted = [ (a ^ b) for (a, b) in zip(a1, b1) ]
    return bytes(encrypted)


def isprintable(text):
    printable_chars = bytes(string.printable, 'ascii')
    printable = all(char in printable_chars for char in text)
    return printable


for key in range(0x100):
    a = x
    b = cycle(bytes([key]))
    result = bxor(a, b)

    # if isprintable(result) and b'}' in result and b'{' in result:
    if b'encryptCTF' in result:
        print(result)
