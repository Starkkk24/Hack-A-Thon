import requests

url = "http://127.0.0.1:5500/sell/web/add"
data1 = {
    "user": "zt",
    "name": "saswath",
    "dept": "site",
    "code": "hello",
    "under": "zzzz"
}
params = {
    "userid": "22832",
    "code": "dsfghjk"
}

data = {
        
        'under': 'MGKKT',
        
    }
# response = requests.get(url, params=params)
# response = requests.post(url, data=data)
# print(response.text)
url = "http://127.0.0.1:5500/man/web/get-site"
response = requests.post(url, data=data)
print(response.text)