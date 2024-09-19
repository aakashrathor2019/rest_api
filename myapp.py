import requests
import json

URL = "http://127.0.0.1:8001/api1/student/"

data = {
    'name': 'Ram',
    'roll': 10,
    'city': 'Barwaha',
    'email': 'r@gmail.com'
}

json_data = json.dumps(data)

# Corrected the request to include headers
r = requests.post(url=URL, data=json_data, headers={'Content-Type': 'application/json'})

print("Status Code:", r.status_code)
print("Response Text:", r.text)

try:
    data = r.json()
    print("Response JSON:", data)
except ValueError:
    print("Response is not in JSON format")
