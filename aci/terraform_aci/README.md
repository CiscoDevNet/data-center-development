# Automate ACI with Terraform

## Overview

**ACI Terraform Provider**: Use Terraform with the [Cisco ACI provider](https://registry.terraform.io/providers/CiscoDevNet/aci/latest) to automate the provisioning and management of ACI resources. This allows for infrastructure as code (IaC) practices.
Example Terraform Configuration:

<br>

## Usage

- Change directories into your config of choice

```
(venv) alexstev@ALEXSTEV-M-FCUD terraform_aci % cd get_aci_system 
(venv) alexstev@ALEXSTEV-M-FCUD get_aci_system %
```

<br>

- Run these Terraform commands, in this sequence:

> Note: these results shown are for the **get_aci_system** config

<br>

```bash
terraform init
```

![image](https://github.com/user-attachments/assets/1fd27b4e-6e6e-48b6-86d8-2f8f983f252f)


```bash
terraform plan
```

![image](https://github.com/user-attachments/assets/9480a41a-e178-4232-931c-8733d0e6224c)


```bash
terraform apply
```

![image](https://github.com/user-attachments/assets/9dd79a3f-6b66-43fb-be97-98603da4ea26)




