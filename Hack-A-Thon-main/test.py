import requests

url = "http://192.168.214.161:5000/auth/web/reg"
data = {
    "key1": "value1",
    "key2": "value2"
}

response = requests.post(url, data=data)
print(response.text)
