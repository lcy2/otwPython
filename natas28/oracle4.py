import requests
import string
import urllib
import sys
import base64
import re


# In this oracle, i'm trying to edit the last byte to reveal the message
# this is by attempting to get the plaintext of the last byte to be 0x01
# therefore the stinger must be the Message xor 0x01 xor ciphertext
# or M xor 0x01 xor C

target = 'http://natas28.natas.labs.overthewire.org/index.php'
target2 = 'http://natas28.natas.labs.overthewire.org/search.php'


user_auth = ('natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')
#tar = string.ascii_letters + string.digits
tar = ['bbbbbbbbbbbbbb']

# notes
# 32 + 16 + 32 bytes   
# 16 byte blocks
# padding error only happens at the last 16 bytes


header = {'Content-Type': 'application/x-www-form-urlencoded'}








for i in range(0, len(tar)):

    payload = 'query=%s' % tar[i]
    response = requests.post(target, auth = user_auth, headers = header, data = payload, allow_redirects = True)
    query = str.split(response.url.encode('ascii','ignore'), '=')
    #print response.url
    #print response.url.encode('ascii', 'ignore')
    #print(base64.b64decode(urllib.unquote(query[1]))), 
    #print(len((base64.b64decode(urllib.unquote(query[1])))))
    
    # find where the blocks start and end
    urlgetvar = base64.b64decode(urllib.unquote(query[1]))
    bytesarray = [ord(x) for x in urlgetvar]
    #print urlgetvar
    #print bytesize
    

    # which byte to change


    prevbytes = [111,42,47]

    # the story so far:
    print [chr(x) for x in prevbytes]
    print prevbytes
    print

    changebyte = bytesarray[-(len(prevbytes) + 1)]

    for i in range(0,256):
        bytesarray[-(len(prevbytes) + 1)] = changebyte ^ (len(prevbytes) + 1) ^ i
        bytesarray[-(len(prevbytes)):] = prevbytes
        rejoinarray = bytesarray[:]
        
        # put together the query string
        rejoinarray = [chr(x) for x in rejoinarray]
        

        rejoined = urllib.quote_plus(base64.b64encode("".join(rejoinarray)))


        padres = requests.get(target2+"/?query="+rejoined, auth = user_auth, headers = header)
        query2 = str.split(padres.url.encode('ascii','ignore'), '=')
        #print(base64.b64decode(urllib.unquote(query2[1]))), 
        #print(len((base64.b64decode(urllib.unquote(query2[1])))))




        #print padres.url
        #print padres.text

        padressplits = str.split(str(padres.text), '\n')
        print padressplits[-1],


        if re.search('PKCS', padres.text) != None: # if i can't find the PKCS error msg,
            print "Pad Error",
        else:
            print "Error Free",
        print str(i).zfill(3)
        
        

    #print(urllib.unquote(query[1])),
    #print(urllib.unquote(tar[i]).ljust(2))
