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


<br>

## List of Configs

1. **get_aci_system**

It uses the [aci_system](https://registry.terraform.io/providers/CiscoDevNet/aci/latest/docs/data-sources/system) data source of the [aci provider](https://registry.terraform.io/providers/CiscoDevNet/aci/latest/docs) from Cisco DevNet to return the complete data source for the ACI system, e.g.

```
aci_system = {
  "address" = "10.0.0.1"
  "boot_strap_tate" = tostring(null)
  "child_action" = ""
  "config_issues" = ""
  "control_plane_mtu" = "9000"
  "current_time" = "2024-07-25T20:08:29.911+00:00"
  "enforce_subnet_check" = "no"
  "etep_addr" = "0.0.0.0"
  "fabric_domain" = "ACI Fabric1"
  "fabric_id" = "1"
  "fabric_mac" = "00:22:BD:F8:19:FF"
  "id" = "topology/pod-1/node-1/sys"
  "inb_mgmt_addr" = "192.168.11.1"
  "inb_mgmt_addr6" = "fc00::1"
  "inb_mgmt_addr6_mask" = "0"
  "inb_mgmt_addr_mask" = "24"
  "inb_mgmt_gateway" = "192.168.11.254"
  "inb_mgmt_gateway6" = "::"
  "last_reboot_time" = "2024-07-24T21:59:38.996+00:00"
  "last_reset_reason" = "unknown"
  "lc_own" = "local"
  "mod_ts" = "2024-07-25T19:26:13.694+00:00"
  "mode" = "unspecified"
  "mon_pol_dn" = "uni/fabric/monfab-default"
  "name" = "apic1"
  "name_alias" = ""
  "node_type" = "unspecified"
  "oob_mgmt_addr" = "10.10.20.14"
  "oob_mgmt_addr6" = "fe80::200:ff:fe0:0"
  "oob_mgmt_addr6_mask" = "0"
  "oob_mgmt_addr_mask" = "24"
  "oob_mgmt_gateway" = "10.10.20.254"
  "oob_mgmt_gateway6" = "2001:420:28e:2020:acc:68ff:fe28:b540"
  "pod_id" = "1"
  "remote_network_id" = "0"
  "remote_node" = "no"
  "rl_oper_pod_id" = "0"
  "rl_routable_mode" = "no"
  "rldirect_mode" = "no"
  "role" = "controller"
  "serial" = "TEP-1-1"
  "server_type" = "unspecified"
  "site_id" = "0"
  "state" = "in-service"
  "system_id" = "1"
  "system_uptime" = "00:22:08:51.000"
  "tep_pool" = "0.0.0.0"
  "unicast_xr_ep_learn_disable" = "no"
  "version" = "6.0(2h)"
  "virtual_mode" = "no"
}
```


