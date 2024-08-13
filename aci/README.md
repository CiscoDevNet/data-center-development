<h1 align="center">Application Centric Infrastructure (ACI) Data Center Development</h1>
<p align="center">
<img src="https://github.com/user-attachments/assets/c40205eb-4ec5-4491-bdb6-7cfc495451af" width="150">
</p>


Welcome to the ACI portion of the Data Center Development repository! This section contains automation scripts and configurations for managing Cisco ACI and Nexus Dashboard environments.


## Table of Contents

- [ansible_aci](./ansible_aci/): Directory for Ansible playbooks and roles specific to ACI automation.
  
- [mso_aci](./mso_aci/): Scripts and documentation related to Cisco Multi-Site Orchestrator (MSO) for ACI.
  
- [nexus_dashboard](./nexus_dashboard/):
  - [ansible_nexus_dashboard](./nexus_dashboard/ansible_nexus_dashboard/): Ansible playbooks for Nexus Dashboard automation.
  - [ndfc](./nexus_dashboard/ndfc/): Scripts and documentation for Nexus Dashboard Fabric Controller (NDFC).
  - [ndo](./nexus_dashboard/ndo/): Scripts and documentation for Nexus Dashboard Orchestrator (NDO).
  - [python_nexus_dashboard](./nexus_dashboard/python_nexus_dashboard/): Python scripts for automation tasks related to Nexus Dashboard.
  - [terraform_nexus_dashboard](./nexus_dashboard/terraform_nexus_dashboard/): Terraform configurations for Nexus Dashboard.

- [python_scripting_aci](./python_scripting_aci/):
  - [aci_cobra_sdk](./python_scripting_aci/aci_cobra_sdk/): Scripts utilizing ACI COBRA SDK for automation.
  - [aci_toolkit](./python_scripting_aci/aci_toolkit/): Scripts utilizing ACI Toolkit for automation.

- [terraform_aci](./terraform_aci/): Directory for Terraform configurations specific to Cisco ACI.


<br>

## Overview 

For ACI, we will be utilizing the [ACI Simulator Always-On sandbox](https://devnetsandbox.cisco.com/DevNet/catalog/Open-NX-OS-Programmability_open-nx-os) from Cisco DevNet. 

Here is the infrastructure of the sandbox:

![image](https://github.com/user-attachments/assets/ec42f2eb-93ab-4b30-9fa2-0173e5802605)



In addition, DevNet also offers a *Reservable* [ACI Simulator 6.0 sandbox](https://devnetsandbox.cisco.com/DevNet/catalog/aci-simulator-sandbox_aci-simulator), although we don not make use of it in this repo.

> **Note**: If you want to learn more about ACI, check out these [FREE ACI Learning Labs](https://developer.cisco.com/learning/search/?categories=Data%20Center&contentType=track,module,lab&page=1&products=ACI) from DevNet.


<br>

## Prerequisites

- You should have an enviornment with ACI running. This could be a physical setup with APIC, a DevNet sandbox, or [ACI Simulator](https://www.cisco.com/c/en/us/products/cloud-systems-management/application-centric-infrastructure-simulator/index.html) software.
- An IDE (e.g. VS Code)

<br>

## Lab Setup: utilizing the [ACI Simulator Always-On sandbox](https://devnetsandbox.cisco.com/DevNet/catalog/ACI-Simulator-Always-On_aci-simulator-always-on) from DevNet

- Navigate to [APIC](https://devnetsandbox.cisco.com/DevNet/catalog/ACI-Simulator-Always-On_aci-simulator-always-on) and login with the following credentials:

```
admin
```
```
!v3G@!4@Y
```

<br>

- Observe the APIC:

![image](https://github.com/user-attachments/assets/e49b658e-5dc3-4817-a8a1-48bc372622be)




<br>

## Next Steps

Once you've stablished connectivity between your local system and the Nexus 9k, you can proceed to the labs in this directory.

