import requests

url = "http://192.168.214.161:5000/auth/web/log"
data = {
    "user": "z",
    "name": "saswath",
    "dept": "Normal",
    "code": "hello",
    "under": "zzzz"
}
params = {
    "userid": "z",
    "code": "hello1"
}
response = requests.get(url, params=params)
# response = requests.post(url, data=data)
print(response.text)
