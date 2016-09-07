import random
import string

chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
for i in range(0,100):
    print "".join(random.choice(chars) for _ in range(10))
