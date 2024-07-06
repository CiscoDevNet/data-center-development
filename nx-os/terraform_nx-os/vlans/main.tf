terraform {
  required_providers {
    nxos = {
      source  = "CiscoDevNet/nxos"
      version = "0.1.0"
    }
  }
}

# Provider configuration using environment variables for credentials
provider "nxos" {
  username = var.nxos_username
  password = var.nxos_password
  url      = var.nxos_url
  insecure = var.nxos_insecure
}

# VLAN 102 configuration for Ethernet1/2
resource "nxos_vlan" "eth1_2_vlan" {
  vlan_id = 102
  name    = "Ethernet1/2"
  state   = "active"
}

# VLAN 103 configuration for Ethernet1/3
resource "nxos_vlan" "eth1_3_vlan" {
  vlan_id = 103
  name    = "Ethernet1/3"
  state   = "active"
}

# VLAN 104 configuration for Ethernet1/4
resource "nxos_vlan" "eth1_4_vlan" {
  vlan_id = 104
  name    = "Ethernet1/4"
  state   = "active"
}

# Interface configuration for Ethernet1/2
resource "nxos_interface" "eth1_2" {
  name            = "Ethernet1/2"
  description     = "Configured by Terraform"
  enabled         = true
  switchport_mode = "access"
  access_vlan     = nxos_vlan.eth1_2_vlan.vlan_id
}

# Interface configuration for Ethernet1/3
resource "nxos_interface" "eth1_3" {
  name            = "Ethernet1/3"
  description     = "Configured by Terraform"
  enabled         = true
  switchport_mode = "access"
  access_vlan     = nxos_vlan.eth1_3_vlan.vlan_id
}

# Interface configuration for Ethernet1/4
resource "nxos_interface" "eth1_4" {
  name            = "Ethernet1/4"
  description     = "Configured by Terraform"
  enabled         = true
  switchport_mode = "access"
  access_vlan     = nxos_vlan.eth1_4_vlan.vlan_id
}
