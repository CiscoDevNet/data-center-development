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

resource "nxos_physical_interface" "eth1_7" {
  interface_id             = "eth1/7"
  admin_state              = "up"
  description              = "Configured by Terraform"
  duplex                   = "auto"
  speed                    = "auto"
  mtu                      = 1500
  mode                     = "access"
  native_vlan              = "unknown"
  access_vlan              = "unknown"
  trunk_vlans              = "1-4094"
  fec_mode                 = "auto"
  auto_negotiation         = "on"
  bandwidth                = 1000
  delay                    = 10
  link_logging             = "enable"
  link_debounce_down       = 200
  link_debounce_up         = 0
  medium                   = "broadcast"
  layer                    = "Layer3"
  speed_group              = "auto"
  uni_directional_ethernet = "disable"
  user_configured_flags    = "admin_layer,admin_mtu,admin_state"
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


resource "nxos_physical_interface" "eth1_8" {
  interface_id             = "eth1/8"
  admin_state              = "up"
  description              = "Configured by Terraform"
  duplex                   = "auto"
  speed                    = "auto"
  mtu                      = 1500
  mode                     = "access"
  native_vlan              = "unknown"
  access_vlan              = "unknown"
  trunk_vlans              = "1-4094"
  fec_mode                 = "auto"
  auto_negotiation         = "on"
  bandwidth                = 1000
  delay                    = 10
  link_logging             = "enable"
  link_debounce_down       = 200
  link_debounce_up         = 0
  medium                   = "broadcast"
  layer                    = "Layer3"
  speed_group              = "auto"
  uni_directional_ethernet = "disable"
  user_configured_flags    = "admin_layer,admin_mtu,admin_state"
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

resource "nxos_physical_interface" "eth1_9" {
  interface_id             = "eth1/9"
  admin_state              = "up"
  description              = "Configured by Terraform"
  duplex                   = "auto"
  speed                    = "auto"
  mtu                      = 1500
  mode                     = "access"
  native_vlan              = "unknown"
  access_vlan              = "unknown"
  trunk_vlans              = "1-4094"
  fec_mode                 = "auto"
  auto_negotiation         = "on"
  bandwidth                = 1000
  delay                    = 10
  link_logging             = "enable"
  link_debounce_down       = 200
  link_debounce_up         = 0
  medium                   = "broadcast"
  layer                    = "Layer3"
  speed_group              = "auto"
  uni_directional_ethernet = "disable"
  user_configured_flags    = "admin_layer,admin_mtu,admin_state"
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

