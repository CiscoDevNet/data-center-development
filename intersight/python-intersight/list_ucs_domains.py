import requests
import datetime
import hashlib
import hmac
import base64
import os

# Define your API endpoint
url = "https://intersight.com/api/v1/ntp/Policies"

# Load API key and secret from environment variables or elsewhere
api_key = os.getenv("intersight_api_key")
api_secret_key = os.getenv("intersight_api_secret_key")

# Compute the date string in the required format
current_date = datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

# Optional: Compute digest if required by the API
digest = ""
if "{{computed-digest}}" in headers["Digest"]:
    # Compute the digest (e.g., SHA-256 of the request body)
    digest = hashlib.sha256(b"").hexdigest()

# Create the authorization header using HTTP Signature (assuming Signature method)
http_method = "GET"  # Adjust based on your request type
http_path = "/api/v1/ntp/Policies"  # Adjust based on your API endpoint path

signature_string = f"(request-target): {http_method.lower()} {http_path}\nhost: intersight.com\ndate: {current_date}\n"
if digest:
    signature_string += f"digest: {digest}\n"

signature = base64.b64encode(
    hmac.new(
        api_secret_key.encode(), signature_string.encode(), hashlib.sha256
    ).digest()
)

headers = {
    "Accept": "application/json",
    "Authorization": f'Signature keyId="{api_key}",algorithm="hmac-sha256",headers="(request-target) host date",signature="{signature.decode()}"',
    "Digest": f"SHA-256={digest}",
    "Date": current_date,
}

# Make the HTTP request
response = requests.get(url, headers=headers)

# Print response
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.json()}")
