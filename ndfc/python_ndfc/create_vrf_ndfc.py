import requests
import json

# Read the JWT token from the file
with open("ndfc_token.txt", "r") as file:
    jwt_token = file.read().strip()

if not jwt_token:
    raise ValueError("JWT token is not set in the file.")

# Define the API endpoint URL
url = "https://10.10.20.60/appcenter/cisco/ndfc/api/v1/lan-fabric/rest/top-down/v2/fabrics/DevNet_Fabric/vrfs"

# Define the payload for VRF creation without VLAN details
payload = json.dumps(
    {
        "fabric": "DevNet_Fabric",
        "vrfName": "VRF_PYTHON",
        "vrfTemplate": "Default_VRF_Universal",
        "vrfExtensionTemplate": "Default_VRF_Extension_Universal",
        "vrfId": 51000,
        "vrfTemplateConfig": {
            "vrfName": "VRF_PYTHON",
            "vrfSegmentId": 51000,
            "vrfDescription": "vrf from Python",
            # VLAN details are omitted
        },
    }
)

# Define the headers
headers = {"Cookie": f"AuthCookie={jwt_token}", "Content-Type": "application/json"}

# Send the POST request to create the VRF
response = requests.post(url, headers=headers, data=payload, verify=False)

# Print the response
print(f"The following VRF was created: {response.text}")
