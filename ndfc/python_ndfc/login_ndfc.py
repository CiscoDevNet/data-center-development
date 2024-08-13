import requests
import json

url = "https://10.10.20.60/login"

payload = json.dumps(
    {"domain": "local", "userName": "admin", "userPasswd": "1vtG@lw@y"}
)
headers = {
    "Content-Type": "application/json",
}

response = requests.post(url, headers=headers, data=payload, verify=False)

print("Login Response Status Code:", response.status_code)
# print("Login Response Text:", response.text)

# Extract JWT token
response_data = response.json()
jwt_token = response_data.get("jwttoken")

if not jwt_token:
    raise ValueError("JWT token not found in login response.")

# Save the token to a file
with open("ndfc_token.txt", "w") as file:
    file.write(jwt_token)
