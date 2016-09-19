import requests
import string
import urllib
import sys
import base64
import re





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



# delete one byte at a time





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
    
    

    for index, eachbyte in enumerate(bytesarray):
        if index == 0:
            rejoinarray = bytesarray[:]
        else:
            rejoinarray = bytesarray[:-1*index]
        print "Editing: " + "_" * len(rejoinarray)
        # put together the query string
        rejoinarray = [chr(x) for x in rejoinarray]
        
        # alter last byte
        #rejoinarray[-1] = chr(ord(rejoinarray[-1]) ^ 255)

        rejoined = urllib.quote_plus(base64.b64encode("".join(rejoinarray)))


        padres = requests.get(target2+"/?query="+rejoined, auth = user_auth, headers = header)
        query2 = str.split(padres.url.encode('ascii','ignore'), '=')
        #print(base64.b64decode(urllib.unquote(query2[1]))), 
        #print(len((base64.b64decode(urllib.unquote(query2[1])))))




        #print padres.url
        #print padres.text

        padressplits = str.split(str(padres.text), '\n')
        print padressplits[-1]


        if re.search('PKCS', padres.text) != None: # if i can't find the PKCS error msg,
            print "Pad Error",
        else:
            print "Error Free",
        print "Byte index = " + str(index)
        
        

    #print(urllib.unquote(query[1])),
    #print(urllib.unquote(tar[i]).ljust(2))
