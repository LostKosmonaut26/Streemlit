import requests

url="http://127.0.0.1:1000"
json1={
    "login":"1",
    "password":"1"
}
resp=requests.post(url+"/api/v1/SignIn",json=json1)

print(resp.status_code)
token=resp.json().get("access_token")
json_token= {"Authorization": "Bearer " + token}
data=requests.get(url+"/api/v1/Documents",headers=json_token)
dat=data.json()
print(dat)
