# Username for the NX-OS device
variable "nxos_username" {
  description = "Username for the NX-OS device"
  type        = string
  default     = ""
}

# Password for the NX-OS device
variable "nxos_password" {
  description = "Password for the NX-OS device"
  type        = string
  default     = ""
  sensitive   = true
}

# URL of the NX-OS device
variable "nxos_url" {
  description = "URL of the NX-OS device"
  type        = string
  default     = ""
}

# Allow insecure HTTPS client
variable "nxos_insecure" {
  description = "Allow insecure HTTPS client"
  type        = bool
  default     = true
}
