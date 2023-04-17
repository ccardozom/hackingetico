import urllib3

pool = urllib3.HTTPConnectionPool('www.google.com', 80)
response = pool.request('GET', '/')
print(response.status)
print(response.headers)
print(response.data)