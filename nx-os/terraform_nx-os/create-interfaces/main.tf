terraform {
  required_providers {
    nxos = {
      source  = "CiscoDevNet/nxos"
      version = "0.5.3"
    }
  }
}

provider "nxos" {
  username = var.nxos_username
  password = var.nxos_password
  url      = var.nxos_url
  insecure = var.nxos_insecure
}

resource "nxos_ipv4_interface" "eth1_7_interface" {
  vrf          = "default"
  interface_id = "eth1/7"
  drop_glean   = "disabled"
  forward      = "disabled"
  unnumbered   = "unspecified"
  urpf         = "disabled"
}

resource "nxos_ipv4_interface_address" "eth1_7_address" {
  vrf          = "default"
  interface_id = "eth1/7"
  address      = "192.168.247.107/24"
  type         = "primary"
}

resource "nxos_ipv4_interface" "eth1_8_interface" {
  vrf          = "default"
  interface_id = "eth1/8"
  drop_glean   = "disabled"
  forward      = "disabled"
  unnumbered   = "unspecified"
  urpf         = "disabled"
}

resource "nxos_ipv4_interface_address" "eth1_8_address" {
  vrf          = "default"
  interface_id = "eth1/8"
  address      = "192.168.248.108/24"
  type         = "primary"
}

resource "nxos_ipv4_interface" "eth1_9_interface" {
  vrf          = "default"
  interface_id = "eth1/9"
  drop_glean   = "disabled"
  forward      = "disabled"
  unnumbered   = "unspecified"
  urpf         = "disabled"
}

resource "nxos_ipv4_interface_address" "eth1_9_address" {
  vrf          = "default"
  interface_id = "eth1/9"
  address      = "192.168.249.109/24"
  type         = "primary"
}