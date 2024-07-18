

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

Copy the Secret key from your Downloads to this dir (data-center-development/intersight)


### Prepare for Authentication


Export the API Key and Secret Key in the authenticate.py file like so (be sure you're in your virtual environment):

Linux/Mac
```
export intersight_api_key="<your api key>"
export intersight_api_key_file="../<your secret key>.txt"
```

Windows
```
set intersight_api_key=<your api key>
set intersight_api_key_file=..\<your secret key>.txt
```
