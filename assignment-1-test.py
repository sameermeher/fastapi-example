import requests

url = "http://127.0.0.1:8000/multiply"
data = {"a": 2, "b": 3}

response = requests.post(url, json=data)
print(response.json())