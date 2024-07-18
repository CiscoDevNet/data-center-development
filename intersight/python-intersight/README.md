# Automating Cisco Intersight with Python Scripts


## Setup

- Follow the [instructions in the parent directory](https://github.com/xanderstevenson/data-center-development/tree/main/intersight#installation) to clone, install dependencies, and create a virtual environment.

- Make sure to also export your Intersight credentials as detailed on that page as well. Make sure the **intersight_api_key_file** is stored in the [data-center-development/intersight](https://github.com/xanderstevenson/data-center-development/tree/main/intersight) directory.

<br>

## Usage

### 1. Authenticate

```bash
python3 authenticate.py
```

- Results:

```
Reading API key from file: ./my-api-key-SecretKey.txt
Detected EC private key format
API client created successfully
<intersight.api_client.ApiClient object at 0x109040410>
```

### 2. Obtain a list of Boot Policies

```bash
python3 get_boot_policies.py
```

- Results:

```
Reading API key from file: ../my-api-key-SecretKey.txt
Detected EC private key format
API client created successfully
<intersight.api_client.ApiClient object at 0x10be20f50>
+-------------------------------------+-----------------------------------------------------------+
| Boot Policy                         | Description                                               |
+=====================================+===========================================================+
| Demo_Boot                           |                                                           |
+-------------------------------------+-----------------------------------------------------------+
| pol-cohesity-boot-order             |                                                           |
+-------------------------------------+-----------------------------------------------------------+
| BootOrderPolicy                     |                                                           |
+-------------------------------------+-----------------------------------------------------------+
| UCS-SJC-Boot-Policy-VMware-01       |                                                           |
+-------------------------------------+-----------------------------------------------------------+
| UCS-WS-Boot-Policy-Linux-01         | Linux Boot Policy for Cisco dCloud demonstration.         |
+-------------------------------------+-----------------------------------------------------------+
| UCS-WS-Boot-Policy-Windows-01       | Windows Boot Policy for Cisco dCloud demonstration.       |
+-------------------------------------+-----------------------------------------------------------+
| UCS-WS-Boot-Policy-VMware-01        | VMware Boot Policy for Cisco dCloud demonstration.        |
+-------------------------------------+-----------------------------------------------------------+
| UCS-WS-Boot-Policy-Windows-MRAID-01 | Windows MRAID Boot Policy for Cisco dCloud demonstration. |
+-------------------------------------+-----------------------------------------------------------+
| UCS-WS-Boot-Policy-VMware-MRAID-01  | VMware MRAID Boot Policy for Cisco dCloud demonstration.  |
+-------------------------------------+-----------------------------------------------------------+
| BOOT                                |                                                           |
+-------------------------------------+-----------------------------------------------------------+
| Boot-_Demo_Profile                  |                                                           |
+-------------------------------------+-----------------------------------------------------------+
| boot-test                           |                                                           |
+-------------------------------------+-----------------------------------------------------------+
| UCS-M6-BOOT-Policy-01               |                                                           |
+-------------------------------------+-----------------------------------------------------------+
| UCS-SJC-Boot-Policy-VMware-02       |                                                           |
+-------------------------------------+-----------------------------------------------------------+

Complete results saved to: boot_policies_results/boot_policies_2024-07-18_15-42-11.json
```


<br>


## Reference

[intersight-python](https://github.com/CiscoDevNet/intersight-python?tab=readme-ov-file) on Cisco DevNet
