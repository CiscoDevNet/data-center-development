Python Scripts

ACI Toolkit: Cisco provides an ACI Toolkit which is a set of Python libraries and scripts to interact with the ACI fabric.
REST API: Write Python scripts that use the ACI REST API to automate configurations and retrieve information from the ACI fabric.

Example Python Script:

import requests
import json

apic = "https://apic-ip-address"
username = "admin"
password = "password"

# Login to APIC
def login():
    url = f"{apic}/api/aaaLogin.json"
    auth = {"aaaUser": {"attributes": {"name": username, "pwd": password}}}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(auth), headers=headers, verify=False)
    return response.cookies

# Create a tenant
def create_tenant(cookies, tenant_name):
    url = f"{apic}/api/node/mo/uni/tn-{tenant_name}.json"
    tenant = {"fvTenant": {"attributes": {"name": tenant_name}}}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(tenant), headers=headers, cookies=cookies, verify=False)
    return response.status_code

cookies = login()
status = create_tenant(cookies, "example_tenant")
print(f"Tenant creation status: {status}")
