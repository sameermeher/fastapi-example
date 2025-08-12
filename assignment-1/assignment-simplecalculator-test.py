import requests

url = "http://127.0.0.1:8000/calculator"
data = {
  "a": 2,
  "b": 8,
  "operation": "divide"
}

response = requests.post(url, json=data)
print(response.json())