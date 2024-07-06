# Guide to Managing Cisco NX-OS with Terraform

## Table of Contents

1. [Introduction](#introduction)
2. [Usage](#usage)
    1. [Configure the NX-OS Device](#configure-the-nx-os-device)
    2. [Install Terraform](#install-terraform)
    3. [Create a Terraform Configuration](#create-a-terraform-configuration)
    4. [Initialize Terraform](#initialize-terraform)
    5. [Plan and Apply the Configuration](#plan-and-apply-the-configuration)
    6. [Verify the Configuration](#verify-the-configuration)
3. [Terraform Plans](#terraform-plans)

## Introduction

In this guide, we will set up and manage network infrastructure on Cisco NX-OS devices using Terraform. We will cover the following steps:

1. Configuring the NX-OS device to enable the NX-API feature.
2. Installing Terraform on your local machine.
3. Creating a Terraform configuration file (`main.tf`) to manage interfaces and VLANs on the NX-OS device.
4. Using a `.gitignore` file to exclude sensitive information and unnecessary files from version control.
5. Using a `terraform.tfvars` file to manage variables securely.
6. Initializing, planning, and applying the Terraform configuration.
7. Verifying the configuration on the NX-OS device.


## Usage

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


## Terraform Plans: 

**1. [vlans](https://github.com/xanderstevenson/data-center-development/tree/main/nx-os/terraform_nx-os/vlans)**

In this Terraform plan, we we configure and stand up the first three available Ethernet interfaces. We also create three VLANS with names corresponding to the three interfaces. Each new interface is assigned to the corresponding new VLAN.

