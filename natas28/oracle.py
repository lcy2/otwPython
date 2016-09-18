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
tar = ['bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb']

# notes
# 42 bytes IV?
# 22 bytes blocks
# 44 bytes padding   
# going beyond target length [0, 6], 22 bytes are added to IV
# another 1st block length increase after [7, 14]

# going beyond target length [0, 8], 20 bytes are added in total length
# seems like every 8 length, total length increases. this time by 24 bytes
# seems to alternate between 20 and 24 bytes addition
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
    bytesize = ' '.join(format(ord(x), 'b').zfill(8) for x in urlgetvar)
    #print urlgetvar
    #print bytesize
    
    # cut back 32 bytes
    
    bytesizearray = bytesize.split(' ')
    #lastblock =  bytesizearray[len(bytesizearray)-16:len(bytesizearray)]
    #print lastblock
    sndlastblock = bytesizearray[-48:-32]
    #sndlastblock = bytesizearray[-32:-16]
    #print "check1" + bytesizearray[-17]
    #print sndlastblock
    
    bytereg = []
    
    for i in range(0, 16):   # we're installing this to the end of the padding
        for pre in range(0, i): # prefill padding
            sndlastblock[15-pre] = format(int(sndlastblock[15-pre],2) ^ int(bytereg[pre], 2) ^ (i + 1), 'b').zfill(8)
            print "executed"
        #print sndlastblock
        for j in range(0, 256):  # these are the iterations
            
            
            # attempt to get response using tweaked queries
            guessbyte = format(j, 'b').zfill(8)
            print len(sndlastblock)
            print 'g' + guessbyte,
            print 'snd' + sndlastblock[15-i],
            print '0x' + format(i + 1, 'b').zfill(8),
            # first modify the last byte in the second to last block
            sndlastblock[15-i] = format(int(sndlastblock[15-i],2) ^ int(guessbyte, 2) ^ (i + 1), 'b').zfill(8)
            print 'res' + sndlastblock[15-i],
            # piece together all the blocks
            rejoinarray = bytesizearray[:-16]
            #rejoinarray = bytesizearray[:]
            rejoinarray[-32:-16] = sndlastblock
            #print sndlastblock
            #print rejoinarray
            #print bytesizearray
            

            rejoinarray = [chr(int(x, 2))for x in rejoinarray]
            
            rejoined = urllib.quote_plus(base64.b64encode("".join(rejoinarray)))
            padres = requests.get(target2 + '/?query=' + rejoined, auth = user_auth)
            #print padres.text
            



            query2 = str.split(padres.url.encode('ascii','ignore'), '=')
            #print(urllib.unquote(query2[1]))
            #print(base64.b64decode(urllib.unquote(query2[1]))), 
            #print(len((base64.b64decode(urllib.unquote(query2[1])))))




            #print padres.url
            #print padres.text
            if re.search('PKCS', padres.text) == None: # if i can't find the PKCS error msg,
                print "Found 1 byte",
                print guessbyte
                bytereg.append(guessbyte)
                break
            
        

    #print(urllib.unquote(query[1])),
    #print(urllib.unquote(tar[i]).ljust(2))
