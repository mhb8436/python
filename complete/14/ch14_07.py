import requests

response = requests.get("http://www.naver.com")
print(f"status code : {response.status_code}")
print(f"reponse body : {response.text}")



