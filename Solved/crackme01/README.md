# crackme01
Reversing

## Challenge 

this is crackme01. crackme01 is a crackme. so crackme! Author: @X3eRo0

[crackme01](crackme01)

## Solution

### Crack through reversing the code

Decompiled in Hopper

	int sub_1179(int arg0, int arg1) {
	    printf("Enter The Secret Code To Open the Vault: ");
	    fgets(&var_20, 0x14, *stdin);
	    printf("\nFlag: ");
	    if ((var_1F & 0xff) != 0x44) goto loc_1305;

	loc_11dd:
	    printf(0x203a);
	    if ((var_1E & 0xff) != 0x44) goto loc_1211;

	loc_11f6:
	    printf("cryptCTF{BYE}");
	    rax = exit(0x0);
	    return rax;

	loc_1211:
	    if ((var_1E & 0xff) != 0x1) goto loc_1305;

	loc_121d:
	    printf(0x204b);
	    if ((var_1D & 0xff) != 0x41) goto loc_12fb;

	loc_123a:
	    printf(0x204f);
	    if ((var_1B & 0xff) != 0x20) goto loc_12f1;

	loc_1257:
	    printf(0x2053);
	    if ((var_1A & 0xff) != 0x21) goto loc_12e7;

	loc_1270:
	    printf(0x2057);
	    if ((var_18 & 0xff) != 0x65) goto loc_12dd;

	loc_1289:
	    printf(0x205b);
	    if ((var_17 & 0xff) != 0x19) goto loc_12d3;

	loc_12a2:
	    printf(0x205f);
	    if ((var_16 & 0xff) != 0x9) goto loc_12c9;

	loc_12bb:
	    puts(0x2064);
	    goto loc_1305;

	    //...
	
	}

We can either search for the printf/puts strings and piece it together, or use the variables to solve for the input text.

I did the latter

	# python -c "print '__440141__2021__651909'.replace('_', '0').decode('hex')" | ./crackme01
	Enter The Secret Code To Open the Vault: 
	Flag: encryptCTF{gdb_or_r2?}

### Search for strings

Alteratively, search for strings

	# xxd crackme01 
	...
	00002000: 0100 0200 0000 0000 456e 7465 7220 5468  ........Enter Th
	00002010: 6520 5365 6372 6574 2043 6f64 6520 546f  e Secret Code To
	00002020: 204f 7065 6e20 7468 6520 5661 756c 743a   Open the Vault:
	00002030: 2000 0a46 6c61 673a 2000 656e 0063 7279   ..Flag: .en.cry
	00002040: 7074 4354 467b 4259 457d 0063 7279 0070  ptCTF{BYE}.cry.p
	00002050: 7443 0054 467b 0067 6462 005f 6f72 005f  tC.TF{.gdb._or._
	00002060: 7232 3f00 7d00 0000 011b 033b 3400 0000  r2?.}......;4...

We can see the flag, by removing the null bytes.

	Flag: encryptCTF{BYE}cryptCTF{gdb_or_r2?}


## Flag

	encryptCTF{gdb_or_r2?}
