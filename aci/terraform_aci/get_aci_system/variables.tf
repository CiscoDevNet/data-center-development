variable "aci_username" {
  description = "The username for the ACI API"
  type        = string
}

variable "aci_password" {
  description = "The password for the ACI API"
  type        = string
  sensitive   = true
}

variable "aci_url" {
  description = "The URL of the ACI API endpoint"
  type        = string
}
