import json
from tokenize import String
import requests
import jsonpath
print("*******************************************************************************************")
print("")
print("Add todo")
print("")
api_url = "https://jsonplaceholder.typicode.com/todos/"
todo={"userID":1,"title":'post todo using dumps function',"completed": True}
response= requests.post(api_url,json=todo)
assert response.headers["Content-Type"]=='application/json; charset=utf-8'
print(response.status_code)
print(response.json())
jsonresp=json.loads(response.text)
id=jsonpath.jsonpath(jsonresp,'id')
id=str(id[0])

print("*******************************************************************************************")
print("")
print("Get recently added todo")
api_url = "https://jsonplaceholder.typicode.com/todos/"+id
print("")
response= requests.get(api_url)
print(response.status_code)
print(response.json())

print("*******************************************************************************************")
print("")
print("Update recently added todo using patch")
todo={"title":'Update todo using patch',"completed": False}
response=requests.patch(api_url,json=todo)
print(response.status_code)
print(response.json())

print("*******************************************************************************************")
print("")
print("Update recently added todo using put")
todo={"userID":1,"title":'putopetation on todo using json ',"completed": True}
response=requests.put(api_url,json=todo)
print(response.status_code)


print("*******************************************************************************************")
print("")
print("Delete recently added todo using delete")
response=requests.delete(api_url)
print(response.status_code)


