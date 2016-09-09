import requests
import string
import urllib
import sys


[name, test] = sys.argv

print test


target = 'http://natas28.natas.labs.overthewire.org/index.php'

user_auth = ('natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')
tar = string.ascii_letters + string.digits

# test post data on local netcat: nc -lvp 8888
if test == '1' :
    target = 'http://localhost:8888'
    user_auth = ()
    tar = ['%00']


# test selected stingers
elif test == '2' :
    #tar = ['0', '%00']
    temp = '%{0}'
    tar = []
    for i in range(0, 100):
        tar.append(temp.format(str(i).zfill(2)))

    



header = {'Content-Type': 'application/x-www-form-urlencoded'}


for i in range(0, len(tar)):


    #payload = {'query':'tar[i]'}
    payload = 'query=%s' % tar[i]
    #print payload
    #response = requests.post(target, auth = user_auth, data = payload, allow_redirects = True)
    response = requests.post(target, auth = user_auth, headers = header, data = payload, allow_redirects = True)
    #print(response.text)
    #for rehist in response.history:
#print rehist.status_code, rehist.url
    query = str.split(response.url.encode('ascii','ignore'), '=')
    #print(query)
    print(tar[i]),
    print(urllib.unquote(query[1])),
    print(urllib.unquote(tar[i]))
