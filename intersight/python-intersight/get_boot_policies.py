from api_client import get_api_client
from intersight.api import boot_api
from pprint import pprint
import intersight
import os
import sys
from tabulate import tabulate
import datetime
import json
import pathlib

# Example usage
api_key = os.getenv("intersight_api_key")
api_key_file = os.getenv("intersight_api_key_file")

if not (api_key and api_key_file):
    print("Environment variables for API key or API secret file are not set")
    sys.exit(1)

# Create API client
client = get_api_client(api_key, api_secret_file=api_key_file)

# Create an instance of the API class
api_instance = boot_api.BootApi(client)

try:
    # Example: Read a 'boot.PrecisionPolicy' resource
    api_response = api_instance.get_boot_precision_policy_list()

    # Formatting output into a table
    headers = ["Boot Policy", "Description"]
    table_data = []

    for policy in api_response.results:
        row = [getattr(policy, "name", ""), getattr(policy, "description", "")]
        if hasattr(policy, "enabled") and policy.enabled:
            headers.insert(1, "Enabled")
            row.insert(1, policy.enabled)
        if hasattr(policy, "type") and policy.type:
            headers.append("Type")
            row.append(policy.type)

        table_data.append(row)

    print(tabulate(table_data, headers=headers, tablefmt="grid"))

    # Save complete results to a file with timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    directory = "boot_policies_results"
    pathlib.Path(directory).mkdir(parents=True, exist_ok=True)
    filename = f"boot_policies_{timestamp}.json"
    filepath = os.path.join(directory, filename)

    # Convert datetime object to string
    serialized_response = api_response.to_dict()
    serialized_response["timestamp"] = timestamp

    with open(filepath, "w") as f:
        json.dump(serialized_response, f, default=str, indent=4)

    print(f"\nComplete results saved to: {filepath}")

except intersight.ApiException as e:
    print(f"Exception when calling BootApi->get_boot_precision_policy_list: {e}\n")
