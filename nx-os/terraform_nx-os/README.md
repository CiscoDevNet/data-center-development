# Guide to Managing Cisco NX-OS with Terraform

## Table of Contents

1. [Introduction](#introduction)
2. [Usage](#usage)
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

2. Make sure you've cloned this repo, installed the dependencies from requirments.txt and changed into the directory which contains the Terraform configuration you want to apply.


3. Install Terraform
Download and install Terraform from the Terraform website.


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

**1. [create-interfaces](https://github.com/xanderstevenson/data-center-development/tree/main/nx-os/terraform_nx-os/create-interfaces)**

In this Terraform plan, we configure three Ethernet interfaces with IP addresses and set the administrative state to up.

> Note: sometimes I have to run *terraform apply* twice for all three interfaces to be created. Not sure why. If you know why, please submit a pull request or [raise an issue](https://github.com/xanderstevenson/data-center-development/issues/new).

```
Apply complete! Resources: 3 added, 3 changed, 0 destroyed.
```

Before:

```
Nexus9k(config)# sh ip int br

IP Interface Status for VRF "default"(1)
Interface            IP Address      Interface Status
Eth1/1               192.168.254.101 protocol-up/link-up/admin-up
```


After:

```
Nexus9k(config)# sh ip int br

IP Interface Status for VRF "default"(1)
Interface            IP Address      Interface Status
Eth1/1               192.168.254.101 protocol-up/link-up/admin-up       
Eth1/7               192.168.247.107 protocol-down/link-down/admin-up   
Eth1/8               192.168.248.108 protocol-down/link-down/admin-up   
Eth1/9               192.168.249.109 protocol-down/link-down/admin-up   
Nexus9k(config)# sh ip int br
```

In addition, running **terraform destroy** will remove those three interfaces.


<br>


**1. [create-interfaces](https://github.com/xanderstevenson/data-center-development/tree/main/nx-os/terraform_nx-os/create-vlans)**

This Terraform configuration sets up VLAN interfaces (SVIs) on Cisco NX-OS devices using the CiscoDevNet/nxos provider version 0.5.3. It defines three VLAN interfaces (vlan107, vlan108, and vlan109) with associated SVI (Switched Virtual Interface) configurations, including administrative state, bandwidth, delay, description, medium type, and MTU settings. Each SVI is configured to operate within the default VRF (Virtual Routing and Forwarding) instance (sys/inst-default). Additionally, IPv4 configurations for these interfaces ensure specific behavior such as disabled drop_glean, forwarding, and URPF (Unicast Reverse Path Forwarding). Dependencies between these resources are established to ensure proper provisioning order, adhering to best practices for network infrastructure automation.

After applying this configuration, you can view the VLANS as such:

```
Nexus9k# conf t
Enter configuration commands, one per line. End with CNTL/Z.
Nexus9k(config)# show run interface vlan 107

!Command: show running-config interface Vlan107
!Running configuration last done at: Mon Jul  8 18:13:10 2024
!Time: Mon Jul  8 18:16:11 2024

version 10.3(1) Bios:version  

interface Vlan107
  description My Terraform VLAN
  no shutdown

Nexus9k(config)# show run interface vlan 108

!Command: show running-config interface Vlan108
!Running configuration last done at: Mon Jul  8 18:13:10 2024
!Time: Mon Jul  8 18:16:14 2024

version 10.3(1) Bios:version  

interface Vlan108
  description My Terraform VLAN
  no shutdown

Nexus9k(config)# show run interface vlan 109

!Command: show running-config interface Vlan109
!Running configuration last done at: Mon Jul  8 18:13:10 2024
!Time: Mon Jul  8 18:16:16 2024

version 10.3(1) Bios:version  

interface Vlan109
  description My Terraform VLAN
  no shutdown

Nexus9k(config)#
```





## Resources

[nxos Terraform provider](https://registry.terraform.io/providers/CiscoDevNet/nxos/latest)

