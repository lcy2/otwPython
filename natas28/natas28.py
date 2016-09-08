import requests
import string
target = 'http://natas28.natas.labs.overthewire.org/index.php'
user_auth = ('natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')
tar = string.ascii_letters + string.digits


for i in range(0, len(tar)):
    payload = {'query':tar[i]}
    response = requests.post(target, auth = user_auth, data = payload, allow_redirects = True)
    #print(response.text)
    #for rehist in response.history:
#print rehist.status_code, rehist.url
    query = str.split(response.url.encode('ascii','ignore'), '=')
    print(query[1])
