#!/usr/bin/env python3
import socket

# Adapted from
# http://code.activestate.com/recipes/580691-hamming-error-correction-code/
def hamming_correct(received_bitstring, debug=False):
	# Hamming(7,4) Error Correction Code
	# https://en.wikipedia.org/wiki/Hamming(7%2C4)
	# FB - 20160723
	# the encoding matrix
	G = ['1101', '1011', '1000', '0111', '0100', '0010', '0001']
	# the parity-check matrix
	H = ['1010101', '0110011', '0001111']
	Ht = ['100', '010', '110', '001', '101', '011', '111']
	# the decoding matrix
	R = ['0010000', '0000100', '0000010', '0000001']

	x = received_bitstring
	z = ''.join([str(bin(int(j, 2) & int(x, 2)).count('1') % 2) for j in H])
	if int(z, 2) > 0:
	    e = int(Ht[int(z, 2) - 1], 2)
	else:
	    e = 0
	if debug:
		print('Which bit found to have error (0: no error): ' + str(e))

	# correct the error
	if e > 0:
	    x = list(x)
	    x[e - 1] = str(1 - int(x[e - 1]))
	    x = ''.join(x)

	p = ''.join([str(bin(int(k, 2) & int(x, 2)).count('1') % 2) for k in R])
	if debug:
		print('Corrected output bit string: ' + p)

	return p

def test_cases():
	# https://codegolf.stackexchange.com/questions/45684/correct-errors-using-hamming7-4
	assert hamming_correct("1110000") == "1000"  # no error
	assert hamming_correct("1100000") == "1000"  # error at 1st data bit
	assert hamming_correct("1111011") == "1111"  # error at 2nd data bit
	assert hamming_correct("0110001") == "1011"  # error at 3rd data bit (example)
	assert hamming_correct("1011011") == "1010"  # error at 4th data bit
	assert hamming_correct("0101001") == "0001"  # error at 1st parity bit
	assert hamming_correct("1010000") == "1000"  # error at 2nd parity bit
	assert hamming_correct("0100010") == "0010"  # error at 3rd parity bit
	
if __name__ == '__main__':
    s = socket.socket()
    s.connect(('104.154.106.182', 6969))

    while True:
        data = s.recv(40960).decode()
        if not data:
            break

        print("Received:", data)

        if '[*] CODE: ' in data:
        	received_bits = data.split('CODE: ')[1].splitlines()[0]
        	data_bits = hamming_correct(received_bits)
        	s.send(str(data_bits).encode() + b'\n')

        if 'encryptCTF{' in data:
            quit()
