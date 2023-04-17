import requests, json

print("Requests probando API REST")
response = requests.get("http://httpbin.org/get", timeout=5)
print("Status code: ", response.status_code)
if response.status_code == 200:
    results = response.json()
    for result in results.items():
        print(result)
        
    print("Headers response")
    for header, value in response.headers.items():
        print(header, "--->", value)
        
    print("Headers request")
    for header, value in response.request.headers.items():
        print(header,"==>",value)
    print("Server: " + response.headers['server'])
else:
    print("Error code {}".format(response.status_code))
    
print("--------- Peticion POST ------------")
datos = {'id':'0123456789',}
response = requests.post("http://httpbin.org/post", timeout=5, data=datos)
print("Status code: ", response.status_code)
if response.status_code == 200:
    results = response.json()
    for result in results.items():
        print(result)
        
print("--------- Peticion PATCH ------------")
datos = {'id':'0123456789',}
response = requests.patch("http://httpbin.org/patch", timeout=5, data=datos)
print("Status code: ", response.status_code)
if response.status_code == 200:
    results = response.json()
    for result in results.items():
        print(result)