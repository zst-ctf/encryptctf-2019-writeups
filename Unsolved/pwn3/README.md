# pwn3
Pwn

## Challenge 

libc is such a nice place to hangout, isn't it?

nc 104.154.106.182 4567

author: codacker



## Solution



	undefined4 main(void){
	  char local_90 [140];
	  
	  setvbuf(stdout,(char *)0x0,2,0);
	  puts("I am hungry you have to feed me to win this challenge...\n");
	  puts("Now give me some sweet desert: ");
	  gets(local_90);
	  return 0;
	}


## Flag

	??