import requests
import string
import urllib
import sys
import base64
import re
import difflib

# In this oracle, I will repeatedly submit target texts that
# are smaller and smaller such that i can brute force attack
# the secret key appended behind the chosen plaintext

# in 5c we use parallel comparison + SN2
# assuming the blocks are padded correctly
# make it such that the last block = {unknown} + padding


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




secretkey = ';302%L'
#secretkey = ''

twocharrec = ''

for i in range(7, 33):
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
        print "-" * 60

        # expand the secretkey to be url encoded
        secarray = ["%" + format(ord(x),'x') for x in secretkey[::-1]]
        
        # this is the known query / guessing query
        tar2 = pad + "%" + format(j,'x').zfill(2) + "".join(secarray) + "%{0}".format(format(16-i, "x").zfill(2)) * (16 - i) + ptx * 2 # if something gets magic quoted, i'll know

        #tar2 = pad + chr(j) + secretkey[::-1] + "%0d" * (16 - i) + ptx * 1
        #print "%{0}".format(format(16-i, "x").zfill(2)) * (16 - i)
        #print "%0d" * (16 - i)
        print tar2, len(tar2), (len(tar2) + 32 + 19 + 16)
        # this is the unknown one
        tar3 = pad + ptx * (16 + 3 + i)
        print tar3, len(tar3), len(tar3) + 32 + 19 + 16
        #print "lenghth of tar2: " + str(len(tar2)) + " i = " + str(i)
        
        payload2 = 'query=%s' % tar2
        response2 = requests.post(target, auth = user_auth, headers = header, data = payload2, allow_redirects = True)
        query2 = str.split(response2.url.encode('ascii','ignore'), '=')
        
        urlgetvar2 = base64.b64decode(urllib.unquote(query2[1]))
        bytesarray2 = [ord(x) for x in urlgetvar2]
        
        
        payload3 = 'query=%s' % tar3
        response3 = requests.post(target, auth = user_auth, headers = header, data = payload3, allow_redirects = True)
        query3 = str.split(response3.url.encode('ascii','ignore'), '=')
        
        urlgetvar3 = base64.b64decode(urllib.unquote(query3[1]))
        bytesarray3 = [ord(x) for x in urlgetvar3]
        #print "".join([format(x, 'x').zfill(2) for x in bytesarray2[48:80]]),
        #print " ",
        #print "".join([format(x, 'x').zfill(2) for x in bytesarray2[80:112]]),
        
        
        
        print " " + format(j,'x').zfill(2) + " " + secretkey[::-1] + " " + chr(j)
        


        print len(bytesarray2), len(bytesarray3)

        if len(bytesarray2) > 100:
            twocharrec += format(j,'x').zfill(2) + " "
        tmptxt = ''
        tmptxt2 = ''
        for index, eachchar in enumerate(bytesarray2):
            tmptxt += format(eachchar, 'x').zfill(2)
            tmptxt2 += format(bytesarray3[index], 'x').zfill(2)
            if index % 16 == 15:
                print tmptxt, tmptxt2
                tmptxt = ''
                tmptxt2 = ''
#        a = "".join([format(x, 'x').zfill(2) for x in bytesarray2[64:80]])
#        b = "".join([format(x, 'x').zfill(2) for x in bytesarray2[96:112]])
 
        
#        diff = difflib.ndiff(a, b)
#        totaldiff = ""
#        for diffi, diffitem in enumerate(diff):
#            totaldiff += diffitem
#            #print totaldiff
#            #print str(diffi) + diffitem 
#        if diffi < 5:
#            print totaldiff
         

        #print "\r",

        #print "".join([format(x, 'x').zfill(2) for x in bytesarray2]),
        #if bytesarray2[48:64] != bytesarray2[80:96] :
        #    print "Two char line?"
        #    twochars += chr(j) + " " + str(j) + "\n"
            
        print "".join([format(x, 'x').zfill(2) for x in bytesarray2[48:64]]),
        print " >> ",
        print "".join([format(x, 'x').zfill(2) for x in bytesarray3[96:112]])

        if bytesarray2[48:64] == bytesarray3[96:112] :
            secretkey += chr(j)
            print "breaking"
            break
        if j == 255:
            print "No match :("
            print twocharrec
            sys.exit()
