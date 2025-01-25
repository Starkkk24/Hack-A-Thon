import requests

url = "http://192.168.214.161:5000/auth/web/reg"
data = {
    "user": "sazzzzzzz354",
    "name": "saswath",
    "dept": "Normal",
    "code": "hello",
    "under": "zzzz"
}
params = []
response = requests.get(url, params=params)
response = requests.post(url, data=data)
print(response.text)
