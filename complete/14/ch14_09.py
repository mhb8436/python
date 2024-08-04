import requests

response = requests.get("https://api.github.com")
data = response.json()
for k, v in data.items():
    print(f"{k}: {v}")


