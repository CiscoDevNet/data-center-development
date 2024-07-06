variable "nxos_username" {
  description = "Username for the NX-OS device"
  type        = string
}

variable "nxos_password" {
  description = "Password for the NX-OS device"
  type        = string
  sensitive   = true
}

variable "nxos_url" {
  description = "URL of the NX-OS device"
  type        = string
}

variable "nxos_insecure" {
  description = "Allow insecure HTTPS client"
  type        = bool
  default     = true
}
