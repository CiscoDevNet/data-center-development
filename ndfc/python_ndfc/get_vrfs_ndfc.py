import requests

# Read the JWT token from the file
with open("ndfc_token.txt", "r") as file:
    jwt_token = file.read().strip()

if not jwt_token:
    raise ValueError("JWT token is not set in the file.")

url = "https://10.10.20.60/appcenter/cisco/ndfc/api/v1/lan-fabric/rest/top-down/fabrics/DevNet_Fabric/vrfs"

headers = {"Cookie": f"AuthCookie={jwt_token}"}

response = requests.get(url, headers=headers, verify=False)

print(response.text)
