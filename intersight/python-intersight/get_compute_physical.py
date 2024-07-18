from api_client import get_api_client
from intersight.api import boot_api
from pprint import pprint
import intersight
import os
import sys

# Example usage
api_key = os.getenv("intersight_api_key")
api_key_file = os.getenv("intersight_api_key_file")

if api_key and api_key_file:
    client = get_api_client(api_key, api_secret_file=api_key_file)
else:
    print("Environment variables for API key and key file are not set")
    sys.exit(1)

# Create an instance of the API class
api_instance = boot_api.BootApi(client)

try:
    # Example: Read a 'boot.PrecisionPolicy' resource.
    api_response = api_instance.get_boot_precision_policy_list()
    pprint(api_response)
except intersight.ApiException as e:
    print("Exception when calling BootApi->get_boot_precision_policy_list: %s\n" % e)
