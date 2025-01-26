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
        
        'name': 'Example Item',
        'weight': 12.5,
        'price': 199.99,
        'des': 'This is an example description.',
        'under': 'wert'
    }
# response = requests.get(url, params=params)
response = requests.post(url, data=data)
print(response.text)
