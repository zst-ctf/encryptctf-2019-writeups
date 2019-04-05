import base64
import itertools

ct = 'fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=='
ct = base64.b64decode(ct)
print('ct', ct)

def do_byte_shift(a1, b1):
    encrypted = [ (a - b) for (a, b) in zip(a1, b1) ]
    return bytes(encrypted)

# When we do a calculation between our decoded text, we see
# that the diff is always remaining at \x18
diff = do_byte_shift(ct, b'encryptCTF{')
print('diff', diff)

# hence, use it to calculate a "ceasar cipher"
final = do_byte_shift(ct, itertools.cycle(diff))
print('final', final)

'''
# initially I thought it was ceasar cipher of the base64
# index-lookup table but it was not the case
def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

for rot in range(26):
    x = rot_alpha(rot)(ct)
    try:
        print(x, rot)
        print(base64.b64decode(x))
    except:
        pass
'''
