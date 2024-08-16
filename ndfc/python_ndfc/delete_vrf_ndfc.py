import requests

# Read the JWT token from the file
with open("ndfc_token.txt", "r") as file:
    jwt_token = file.read().strip()

if not jwt_token:
    raise ValueError("JWT token is not set in the file.")

# Define the API base URL
base_url = "https://10.10.20.60/appcenter/cisco/ndfc/api/v1/lan-fabric/rest/top-down/v2/fabrics/DevNet_Fabric"

# Define the VRF and VLAN IDs to be deleted
vrf_name = "VRF_PYTHON"
vlan_id = 2100

# Define the headers
headers = {"Cookie": f"AuthCookie={jwt_token}", "Content-Type": "application/json"}

# Delete the VRF
vrf_url = f"{base_url}/vrfs/{vrf_name}"
response_vrf = requests.delete(vrf_url, headers=headers, verify=False)

if response_vrf.status_code in [200, 204]:
    print(f"Successfully deleted VRF: {vrf_name}")
else:
    print(f"Failed to delete VRF: {response_vrf.status_code} - {response_vrf.text}")

# Delete the VLAN
# vlan_url = f"{base_url}/vlans/{vlan_id}"
# response_vlan = requests.delete(vlan_url, headers=headers, verify=False)

# if response_vlan.status_code in [200, 204]:
#     print(f"Successfully deleted VLAN: {vlan_id}")
# else:
#     print(f"Failed to delete VLAN: {response_vlan.status_code} - {response_vlan.text}")
