terraform {
  required_providers {
    nxos = {
      source  = "CiscoDevNet/nxos"
      version = "0.5.3"
    }
  }
}

provider "nxos" {
  username  = var.nxos_username
  password  = var.nxos_password
  url       = var.nxos_url
  insecure  = var.nxos_insecure
}

resource "nxos_feature_interface_vlan" "feature" {
  admin_state = "enabled"
}

resource "nxos_svi_interface" "sviIf107" {
  interface_id = "vlan107"
  admin_state  = "up"
  bandwidth    = 1000000
  delay        = 1
  description  = "My Terraform VLAN"
  medium       = "bcast"
  mtu          = 1500
  depends_on   = [nxos_feature_interface_vlan.feature]
}

resource "nxos_svi_interface_vrf" "nwRtVrfMbr107" {
  interface_id = "vlan107"
  vrf_dn       = "sys/inst-default"
  depends_on   = [nxos_svi_interface.sviIf107]
}

resource "nxos_ipv4_interface" "ipv4If107" {
  interface_id = "vlan107"
  drop_glean   = "disabled"
  forward      = "disabled"
  unnumbered   = "unspecified"
  urpf         = "disabled"
  vrf          = "default"
  depends_on   = [nxos_svi_interface_vrf.nwRtVrfMbr107]
}

resource "nxos_svi_interface" "sviIf108" {
  interface_id = "vlan108"
  admin_state  = "up"
  bandwidth    = 1000000
  delay        = 1
  description  = "My Terraform VLAN"
  medium       = "bcast"
  mtu          = 1500
  depends_on   = [nxos_feature_interface_vlan.feature]
}

resource "nxos_svi_interface_vrf" "nwRtVrfMbr108" {
  interface_id = "vlan108"
  vrf_dn       = "sys/inst-default"
  depends_on   = [nxos_svi_interface.sviIf108]
}

resource "nxos_ipv4_interface" "ipv4If108" {
  interface_id = "vlan108"
  drop_glean   = "disabled"
  forward      = "disabled"
  unnumbered   = "unspecified"
  urpf         = "disabled"
  vrf          = "default"
  depends_on   = [nxos_svi_interface_vrf.nwRtVrfMbr108]
}

resource "nxos_svi_interface" "sviIf109" {
  interface_id = "vlan109"
  admin_state  = "up"
  bandwidth    = 1000000
  delay        = 1
  description  = "My Terraform VLAN"
  medium       = "bcast"
  mtu          = 1500
  depends_on   = [nxos_feature_interface_vlan.feature]
}

resource "nxos_svi_interface_vrf" "nwRtVrfMbr109" {
  interface_id = "vlan109"
  vrf_dn       = "sys/inst-default"
  depends_on   = [nxos_svi_interface.sviIf109]
}

resource "nxos_ipv4_interface" "ipv4If109" {
  interface_id = "vlan109"
  drop_glean   = "disabled"
  forward      = "disabled"
  unnumbered   = "unspecified"
  urpf         = "disabled"
  vrf          = "default"
  depends_on   = [nxos_svi_interface_vrf.nwRtVrfMbr109]
}
