
1. Configure the NX-OS Device
Ensure the NX-OS device has the NX-API feature enabled. You can do this with the following command on your NX-OS device:

```
feature nxapi
```


2. Install Terraform
Download and install Terraform from the Terraform website.


3. Create a Terraform Configuration
Create a new directory for your Terraform files, and then create a main configuration file, usually named main.tf.

Example main.tf Configuration
Here is an example configuration using the NX-OS provider to manage an interface and a VLAN:

```hcl
terraform {
  required_providers {
    nxos = {
      source  = "CiscoDevNet/nxos"
      version = "0.1.0"
    }
  }
}

provider "nxos" {
  username = "admin"
  password = "password"
  url      = "https://192.168.254.101"
  insecure = true
}

resource "nxos_interface" "eth1" {
  name        = "Ethernet1/1"
  description = "Configured by Terraform"
  enabled     = true
}

resource "nxos_vlan" "vlan10" {
  vlan_id = 10
  name    = "Example_VLAN"
  state   = "active"
}
```


4. Initialize Terraform
Run the following command to initialize Terraform and download the provider plugins:

```
terraform init
```

5. Plan and Apply the Configuration
Run the following commands to see the execution plan and apply the configuration:

```
terraform plan
terraform apply
```

6. Verify the Configuration
After applying the configuration, you can verify the changes on your NX-OS device to ensure they have been correctly applied.
