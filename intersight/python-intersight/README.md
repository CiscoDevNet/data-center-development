# Automating Cisco Intersight with Python Scripts


## Setup

Following the [instructions in the parent directory](https://github.com/xanderstevenson/data-center-development/tree/main/intersight#installation) to clone, install dependencies, and create a virtual environment.

Make sure to also export your Intersight credentials as detailed on that page as well. Make sure the **intersight_api_key_file is stored** in the [data-center-development/intersight](https://github.com/xanderstevenson/data-center-development/tree/main/intersight) directory.

<br>

## Usage

### Authenticate

Run the Authentiction

```bash
python3 authenticate.py
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
