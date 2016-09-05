import requests

payload = {'username' : 'natas17'}

target = 'http://natas17.natas.labs.overthewire.org/index.php?debug=1'

user_auth = ('natas17','8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')

response = requests.post(target, auth = user_auth, data = payload)

print(response.text)
