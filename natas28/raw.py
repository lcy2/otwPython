import requests
import string
import urllib
import sys
import base64





target = 'http://natas28.natas.labs.overthewire.org/index.php'
target2 = 'http://natas28.natas.labs.overthewire.org/search.php' 


user_auth = ('natas28', 'JWwR438wkgTsNKBbcJoowyysdM82YjeF')


tar = ['''1be82511a7ba5bfd578c0eef466db59c
dc84728fdcf89d93751d10a7c75c8cf2
2a527746fe0a5e856c78de40bbf2db07
157d57c994176a05342f0c0b36a3d697
738a5ffb4a4500246775175ae596bbd6
f34df339c69edce11f6650bbced62702''']




#56dc04ae7951bfc0a9d715bc5abc6a95
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
