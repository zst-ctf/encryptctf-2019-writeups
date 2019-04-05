# crackme03
Reversing

## Challenge 

tik-tok tik-tok can you defuse the bomb?

author: codacker
nc 104.154.106.182 7777


## Solution

Decompile in Ghidra and simplify

	undefined4 FUN_00011502(void){
	  code *local_68 [4];
	  code *local_58;
	  undefined local_54 [64];
	  
	  local_68[0] = FUN_00011286;
	  local_68[1] = FUN_000112bd;
	  local_68[2] = FUN_000112e6;
	  local_68[3] = FUN_00011392;
	  local_58 = FUN_00011410;

	  puts("Hi!, i am a BOMB!\nI will go boom if you don\'t give me right inputs");

	  int local_70 = 0;
	  while (local_70 < 5) {
	    printf("Enter input #%d: ",local_70);
	    __isoc99_scanf("%s",local_54);
	    (*local_68[local_70])(local_54);
	    local_70 = local_70 + 1;
	  }
	  FUN_0001122d();
	  return 0;
	}

From this, we see that the 5 inputs must pass the following 5 functions.

	  local_68[0] = FUN_00011286;
	  local_68[1] = FUN_000112bd;
	  local_68[2] = FUN_000112e6;
	  local_68[3] = FUN_00011392;
	  local_58 = FUN_00011410;


They are as follows:

# Function 0

Decompiled

	void FUN_00011286(char *param_1)
	{
	  int iVar1;
	  iVar1 = FUN_000115fc();
	  iVar1 = strcmp(param_1,(char *)(iVar1 + 0xd8e));
	  if (iVar1 != 0) {
	    FUN_00011258();
	  }
	  return;
	}

Notice it checks against a static string in the memory

We can do a strings to find it.

	$ strings crackme03
	// ...
	[^_]
	cat flag.txt
	BOOM!
	Bye!
	CRACKME02
	SUBSCRIBE TO PEWDIEPIE
	Validating Input 4
	you earned it
	Hi!, i am a BOMB!
	I will go boom if you don't give me right inputs
	Enter input #%d: 

And it works

	# python -c 'print "CRACKME02"' | ./crackme03
	Hi!, i am a BOMB!
	I will go boom if you don't give me right inputs
	Enter input #0: Enter input #1: BOOM!
	Bye!

# Function 1

Decompiled

	void FUN_000112bd(int *param_1){
	  FUN_000115fc();
	  if (*param_1 != -0x21524111) {
	    FUN_00011258();
	  }
	  return;
	}

If we convert that integer into positive hex, we get `0xdeadbeef`...

And convert to string with little endian form

	# python -c 'from pwn import *;
		print "CRACKME02"; 
		print p32(0xdeadbeef)' | ./crackme03

	Hi!, i am a BOMB!
	I will go boom if you don't give me right inputs
	Enter input #0: Enter input #1: Enter input #2: BOOM!

# Function 2

Decompiled

	void FUN_000112e6(int param_1)
	{
	  size_t sVar1;
	  uint local_2c;
	  undefined4 local_25, local_21, local_1d, local_19, local_15;
	  undefined local_11;
	  
	  local_25 = 0x7479585a;
	  local_21 = 0x66396255;
	  local_1d = 0x6538376c;
	  local_19 = 0x794a6776;
	  local_15 = 0x4e4a4b33;
	  local_11 = 0;
	  local_2c = 0;

	  while( true ) {
	    sVar1 = strlen((char *)&local_25);
	    if (sVar1 <= local_2c) break;
	    if (*(char *)((int)&local_25 + local_2c) != *(char *)(param_1 + local_2c)) {
	      FUN_00011258(); // print "BOOM!\nBye!"
	    }
	    local_2c = local_2c + 1;
	  }
	  return;
	}

We see that it compares to a dynamically allocated string

	  local_25 = 0x7479585a;
	  local_21 = 0x66396255;
	  local_1d = 0x6538376c;
	  local_19 = 0x794a6776;
	  local_15 = 0x4e4a4b33;

Convert it to string

	p32(0x7479585a)+p32(0x66396255)+p32(0x6538376c)+p32(0x794a6776)+p32(0x4e4a4b33)

And it works

	# python -c 'from pwn import *;
		print "CRACKME02";
		print p32(0xdeadbeef);
		print p32(0x7479585a)+p32(0x66396255)+p32(0x6538376c)+p32(0x794a6776)+p32(0x4e4a4b33);' 
			| ./crackme03

	Hi!, i am a BOMB!
	I will go boom if you don't give me right inputs
	Enter input #0: Enter input #1: Enter input #2: Enter input #3: BOOM!

# Function 3

Decompiled

	void FUN_00011392(char *param_1)
	{
	  size_t sVar1;
	  int iVar2;
	  
	  sVar1 = strlen(param_1);
	  if (3 < sVar1) {
	    FUN_00011258(); // print "BOOM!\nBye!"
	  }
	  iVar2 = atoi(param_1);
	  if ((iVar2 * iVar2 * 2 - iVar2) * 2 + -3 + iVar2 * iVar2 * iVar2 == 0) {
	    puts("SUBSCRIBE TO PEWDIEPIE");
	  }
	  else {
	    FUN_00011258(); // print "BOOM!\nBye!"
	  }
	  return;
	}

Input must be 3 chars which is a digit.

It must fulfill the condition:

	if ((iVar2 * iVar2 * 2 - iVar2) * 2 + -3 + iVar2 * iVar2 * iVar2 == 0) {

	Simplify:
	=>   (2 * x^2 - x) * 2 + -3 + x^3 == 0
	=>   (4 * x^2 - 2*x) - 3 + x^3 == 0
	=>   x^3 + 4*x^2 - 2*x - 3 == 0


Solve for the roots in Wolfram Alpha

- https://www.wolframalpha.com/input/?i=x%5E3+%2B+4*x%5E2+-+2*x+-+3

We get x = 1.

And it works

	# python -c 'from pwn import *;
		print "CRACKME02";
		print p32(0xdeadbeef);
		print p32(0x7479585a)+p32(0x66396255)+p32(0x6538376c)+p32(0x794a6776)+p32(0x4e4a4b33);
		print "1";' 
			| ./crackme03

	Hi!, i am a BOMB!
	I will go boom if you don't give me right inputs
	Enter input #0: Enter input #1: Enter input #2: 
	Enter input #3: SUBSCRIBE TO PEWDIEPIE
	Enter input #4: Validating Input 4

# Function 4

Decompiled

	void FUN_00011410(char *param_1) {
	  char local_1a,local_19,local_18,local_17,local_16,local_15,local_14,local_13,local_12;

	  strncpy(&local_1a,param_1,10);
	  puts("Validating Input 4");
	  if ((int)local_12 + (int)local_1a == 0xd5) {
	    if ((int)local_13 + (int)local_19 == 0xce) {
	      if ((int)local_14 + (int)local_18 == 0xe7) {
	        if ((int)local_15 + (int)local_17 == 0xc9) {
	          if (local_16 == 'i') {
	            puts("you earned it");
	          }
	        }else {
	          FUN_00011258();
	        }
	      }else {
	        FUN_00011258();
	      }
	    }else {
	      FUN_00011258();
	    }
	  }else {
	    FUN_00011258();
	  }

	  return;
	}

Input fulfilling the conditions

	if ((int)local_12 + (int)local_1a == 0xd5) {
	if ((int)local_13 + (int)local_19 == 0xce) {
	if ((int)local_14 + (int)local_18 == 0xe7) {
	if ((int)local_15 + (int)local_17 == 0xc9) {
	if (local_16 == 'i') {

We need to form a payload where the sum of those characters equal that in the condition.

Let's play smart...

	>>> hex(0xd5 - 0x61) # index [0] & [7]
	'0x74'
	
	>>> hex(0xce - 0x61) # index [1] & [6]
	'0x6d'
	
	>>> hex(0xe7 - 0x7d) # index [2] & [5]
	'0x6a'

	>>> hex(0xc9 - 0x61) # index [3] & [4]
	'0x68'


	>>> "746d6a68".decode("hex") + "i" + "617d6161".decode("hex")
	'tmjhia}aa'

And we get the flag

	# python -c '
		from pwn import *;
		print "CRACKME02";
		print p32(0xdeadbeef);
		print p32(0x7479585a)+p32(0x66396255)+p32(0x6538376c)+p32(0x794a6776)+p32(0x4e4a4b33);
		print "1";
		print "tmjhia}aa"  '
		| nc 104.154.106.182 7777

	Hi!, i am a BOMB!
	I will go boom if you don't give me right inputs
	Enter input #0: Enter input #1: Enter input #2:
	Enter input #3: SUBSCRIBE TO PEWDIEPIE
	Enter input #4: Validating Input 4
	you earned it
	encryptCTF{B0mB_D!ffu53d}

## Flag

	encryptCTF{B0mB_D!ffu53d}
