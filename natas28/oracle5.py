import requests
import string
import urllib
import sys
import base64
import re


# In this oracle, I will repeatedly submit target texts that
# are smaller and smaller such that i can brute force attack
# the secret key appended behind the chosen plaintext

target = 'http://natas28.natas.labs.overthewire.org/index.php'
target2 = 'http://natas28.natas.labs.overthewire.org/search.php'


user_auth = ('natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')
#tar = string.ascii_letters + string.digits
pad = 'padpadpadp'
ptx = 'b'

# notes
# 32 + 16 + 32 bytes   
# 16 byte blocks
# padding error only happens at the last 16 bytes


header = {'Content-Type': 'application/x-www-form-urlencoded'}





secretkey = ''


for i in range(1, 33):
    #tar = pad + ptx * (64 - i) + secretkey
    #payload = 'query=%s' % tar
    #response = requests.post(target, auth = user_auth, headers = header, data = payload, allow_redirects = True)
    #query = str.split(response.url.encode('ascii','ignore'), '=')
    #print response.url
    #print response.url.encode('ascii', 'ignore')
    #print(base64.b64decode(urllib.unquote(query[1]))), 
    #print(len((base64.b64decode(urllib.unquote(query[1])))))
    
    #urlgetvar = base64.b64decode(urllib.unquote(query[1]))
    #bytesarray = [ord(x) for x in urlgetvar]
    #print urlgetvar
    #print bytesize 

    
    # experimental block is from [80:112]
    # plaintext block is from [48:80]
    
    for j in range(0,256):

        
        tar2 = pad + ptx * (32 - i) + secretkey +\
            chr(j) + ptx * (32 - i + 1)
        print "lenghth of tar2: " + str(len(tar2))
        
        payload2 = 'query=%s' % tar2
        response2 = requests.post(target, auth = user_auth, headers = header, data = payload2, allow_redirects = True)
        query2 = str.split(response2.url.encode('ascii','ignore'), '=')
        
        urlgetvar2 = base64.b64decode(urllib.unquote(query2[1]))
        bytesarray2 = [ord(x) for x in urlgetvar2]
        print "".join([format(x, 'x').zfill(2) for x in bytesarray2[48:80]]),
        print " ",
        print "".join([format(x, 'x').zfill(2) for x in bytesarray2[80:112]]),
        print " " + format(j,'x').zfill(2) + " " + chr(j) + " " + secretkey
        
        tmptxt = ''
        for index, eachchar in enumerate(bytesarray2):
            tmptxt += format(eachchar, 'x').zfill(2)
            if index % 16 == 15:
                print tmptxt
                tmptxt = ''

        #print "\r",

        #print "".join([format(x, 'x').zfill(2) for x in bytesarray2]),

        if bytesarray2[48:80] == bytesarray2[80:112] :
            secretkey += chr(j)
            break


    print "No match :("
    break
