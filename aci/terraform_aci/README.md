Terraform

ACI Terraform Provider: Use Terraform with the Cisco ACI provider to automate the provisioning and management of ACI resources. This allows for infrastructure as code (IaC) practices.
Example Terraform Configuration:


provider "aci" {
  username = "admin"
  password = "password"
  url      = "https://apic-ip-address"
}

resource "aci_tenant" "example_tenant" {
  name        = "example_tenant"
  description = "Example ACI tenant"
}
