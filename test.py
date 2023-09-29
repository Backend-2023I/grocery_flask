import requests

url  = "http://127.0.0.1:5000/grocery/add"
data = {
    "name": "Milk",
    "quantity": 5,
    "price": 3.5,
    "type": "Fruit"
}
r = requests.post(url, json=data)

print(r.json())