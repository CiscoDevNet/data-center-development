import intersight
import re
import sys
import os


def get_api_client(
    api_key_id,
    api_secret_file=None,
    private_key_string=None,
    endpoint="https://intersight.com",
):
    if api_secret_file is None and private_key_string is None:
        print(
            "Either api_secret_file or private_key_string is required to create api client"
        )
        sys.exit(1)
    if api_secret_file is not None and private_key_string is not None:
        print("Please provide only one among api_secret_file or private_key_string")
        sys.exit(1)

    if api_secret_file is not None:
        print(f"Reading API key from file: {api_secret_file}")
        with open(api_secret_file, "r") as f:
            api_key = f.read()
    else:
        print("Using provided private key string")
        api_key = private_key_string

    if re.search("BEGIN RSA PRIVATE KEY", api_key):
        print("Detected RSA private key format")
        # API Key v2 format
        signing_algorithm = intersight.signing.ALGORITHM_RSASSA_PKCS1v15

    elif re.search("BEGIN EC PRIVATE KEY", api_key):
        print("Detected EC private key format")
        # API Key v3 format
        signing_algorithm = (
            intersight.signing.ALGORITHM_ECDSA_MODE_DETERMINISTIC_RFC6979
        )
    else:
        print("Unsupported private key format")
        sys.exit(1)

    configuration = intersight.Configuration(
        host=endpoint,
        signing_info=intersight.signing.HttpSigningConfiguration(
            key_id=api_key_id,
            private_key_string=api_key,
            signing_scheme=intersight.signing.SCHEME_HS2019,
            signing_algorithm=signing_algorithm,
            hash_algorithm=intersight.signing.HASH_SHA256,
            signed_headers=[
                intersight.signing.HEADER_REQUEST_TARGET,
                intersight.signing.HEADER_HOST,
                intersight.signing.HEADER_DATE,
                intersight.signing.HEADER_DIGEST,
            ],
        ),
    )
    # if you want to turn off certificate verification
    # configuration.verify_ssl = False

    api_client = intersight.ApiClient(configuration)
    print("API client created successfully")
    print(api_client)
    return api_client


# Example usage
api_key = os.getenv("intersight_api_key")
api_key_file = os.getenv("intersight_api_key_file")

if api_key and api_key_file:
    client = get_api_client(api_key, api_secret_file=api_key_file)
else:
    print("Environment variables for API key and key file are not set")
    sys.exit(1)
