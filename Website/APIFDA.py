import requests
url = "https://api.fda.gov/drug/event.json"
response = requests.get(url)
print("status_code", response.status_code)
response_dict = response.json()
print(response_dict.keys())