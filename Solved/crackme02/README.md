# crackme02
Reversing

## Challenge 
quack me!

author: Robyn12

## Solution

Decompile in Ghidra and simplify


	undefined8 FUN_001007d8(void){
	  uint local_38;
	  int local_34;
	  int local_30;
	  byte local_2b [9];
	  byte local_22 [9];
	  byte abStack25 [9];
	  local_38 = 0;
	  puts("Hey give username");
	  read(0,local_22,8);
	  puts("Give pass:");
	  read(0,local_2b,8);
	  local_34 = 0;
	  while (local_34 < 9) {
	    abStack25[(long)local_34] = local_2b[(long)local_34] ^ local_22[(long)local_34];
	    local_34 = local_34 + 1;
	  }
	  local_30 = 0;
	  while (local_30 < 9) {
	    local_38 = local_38 + (int)(char)abStack25[(long)local_30] + local_30 * -4;
	    local_30 = local_30 + 1;
	  }
	  FUN_0010073a((ulong)local_38);

	  return 0;
	}

	undefined8 FUN_0010073a(uint uParm1){
	  int local_3c;
	  undefined8 local_38;
	  undefined8 local_30;
	  undefined8 local_28;
	  undefined4 local_20;
	  undefined2 local_1c;
	  undefined local_1a;

	  local_38 = 0x2e191d141f0e0308; // 2e191d141f0e0308
	  local_30 = 0x1f020a012c162b39; // 1f020a012c162b39
	  local_28 = 0x203401e00051904;  // 0203401e00051904
	  local_20 = 0xc084019;          // 0c084019
	  local_1c = 0x141e;             // 141e
	  local_1a = 0x10;               // 10
	  local_3c = 0;
	  while (local_3c < 0x1f) {
	    putchar((int)*(char *)((long)&local_38 + (long)local_3c) ^ uParm1);
	    local_3c = local_3c + 1;
	  }
	  return 0;
	}


FUN_001007d8
- input `username` of 9 char
- input `pass` of 9 char
- XOR cipher `username` and `pass` together into buffer
- for each char in buffer, calculate SUM of `buffer[i]-4*i` 
- then pass to `FUN_0010073a`

FUN_0010073a
- print XOR cipher of `local_38` through `local_1a` buffer with SUM

Hence we can simply ignore username and password and bruteforce the single key XOR cipher of FUN_0010073a.

	 $ python3 solve.py 
	b'encryptCTF{Algorithms-not-easy}'

## Flag

	encryptCTF{Algorithms-not-easy}
