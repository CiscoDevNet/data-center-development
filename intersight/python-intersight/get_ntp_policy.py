import os
import requests
import json
import datetime
import hashlib
import base64

# Load API key and secret from environment variables
api_key = os.getenv("intersight_api_key")
api_key_file = os.getenv("intersight_api_key_file")

# Check if both API key and API key file are available
if not api_key or not api_key_file:
    raise ValueError(
        "Intersight API key and API key file must be set in environment variables."
    )

# Load RSA private key from file
with open(api_key_file, "rb") as key_file:
    private_key_data = key_file.read()

# Prepare the request payload
url = "https://intersight.com/api/v1/iam/ApiKeys"
payload = json.dumps({"Purpose": "API Key Create"})

# Compute the date string in the required format
current_date = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

# Compute the SHA-256 digest of the payload
digest = hashlib.sha256(payload.encode()).hexdigest()

# Construct the headers
headers = {
    "Accept": "application/json",
    "Authorization": f'Signature keyId="{api_key}",algorithm="rsa-sha256",headers="(request-target) host date digest",signature="Placeholder"',
    "Digest": f"SHA-256={digest}",
    "Date": current_date,
    "Content-Type": "application/json",
}

# Make a POST request with placeholder signature
response = requests.post(url, headers=headers, data=payload)

# Print response
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.json()}")
