import requests

url = "http://127.0.0.1:8000"
data = {
  "username": "sameer",
  "password": "mehersdsdsds",
  "email": "sam@example.com"
}

response = requests.post(f"{url}/register", json=data)
print(response.json())


response = requests.get(f"{url}/users")
print(response.json())