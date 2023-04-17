import http.client as httplib

h = httplib.HTTPConnection('www.google.com')
h.request('GET', '/index.html', headers={'Accept': 'text/html,text/plain'})
response = h.getresponse()
print(response.status)
data = response.read()
print(data)
h.close()