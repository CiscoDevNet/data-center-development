terraform {
  required_providers {
    aci = {
      source  = "ciscodevnet/aci"
      version = "~> 2.15.0"  # Adjust version as needed
    }
  }
}

provider "aci" {
  username = var.aci_username
  password = var.aci_password
  url      = var.aci_url
  insecure = true  # Set to false in production
}

data "aci_system" "system" {
  pod_id    = "1"   # Replace with your actual pod ID
  system_id = "1"   # Replace with your actual system ID
}

output "aci_system" {
  value = data.aci_system.system
}