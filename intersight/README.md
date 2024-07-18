

## Installation

### Clone and Install Dependencies

Follow the instructions on the [main landing page of this repo](https://github.com/xanderstevenson/data-center-development/tree/main) to clone it and install dependencies.

Change into this directory:

```bash
cd https://github.com/xanderstevenson/data-center-development/intersight
```

Install the Intersight library

```bash
pip install intersight
```

### Claim dCloud Intersight Pod and API Keys

Go to Cisco Intersight - Manage Infrastructure from the Cloud v1 

https://dcloud2-rtp.cisco.com/content/instantdemo/cisco-intersight-infrastructure-services


Enter Intersight

![image](https://github.com/user-attachments/assets/fb3394f8-c677-41a1-8b8e-157308f6d555)


From the top menu, choose `System`

![image](https://github.com/user-attachments/assets/cebef1ea-f554-4d05-bd88-0cb5a4242d8e)


Choose Generate API Key > version 3 (giving it any name and expiration > copy API Key ID and save the Secret Key.

Copy the Secret key to this dir (data-center-development/intersight)


### Prepare Python Script for Authentication


Export the API Key and Secret Key in the authenticate.py file like so (be sure you're in your virtual environment):

Linux/Mac
```
export api_key="59bc454c16267c000192f683/669867d4756461330157a6fc/66986e087564613101976ffd"
export api_key_file="path/to/my-api-key-SecretKey.txt"
```

Windows
```
set export api_key=59bc454c16267c000192f683/669867d4756461330157a6fc/66986e087564613101976ffd
set api_key_file=path\to\my-api-key-SecretKey.txt
```

## Usage

### Authenticate

Run the Authentiction

```bash
python3 auhtenticate.py
```

the reuslts should be similar to:

```
Reading API key from file: ./my-api-key-SecretKey.txt
Detected EC private key format
API client created successfully
<intersight.api_client.ApiClient object at 0x109040410>
```



## Reference

[intersight-python](https://github.com/CiscoDevNet/intersight-python?tab=readme-ov-file) on Cisco DevNet

