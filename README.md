<h1 align="center">Data Center Development</h1>
<p align="center">
<img src="https://github.com/user-attachments/assets/50a5b0ea-63f1-4565-88ce-75764876b3ec" width="200">
</p>

## Project Description

This is a repository for code and instructions to help you interact with and automate Cisco Data Center technologies, such as [Data Center Switches](https://www.cisco.com/site/us/en/products/networking/cloud-networking-switches/index.html), [NX-OS](https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/nx-os-software/data_sheet_c78-652063.html?dtid=osscdc000283), [Application Centric Infrastructure (ACI)](https://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/application-centric-infrastructure/solution-overview-c22-741487.html), [Unified Computing System (UCS)](https://www.cisco.com/site/us/en/products/computing/servers-unified-computing-systems/index.html), [Intersight](https://intersight.com/), [Nexus Dashboard Facbric Controller (NDFC)](https://www.cisco.com/c/en/us/products/collateral/cloud-systems-management/prime-data-center-network-manager/at-a-glance-c45-741113.html), and more.

The code in these directories was primarily tested against the free [sandboxes from Cisco DevNet](https://devnetsandbox.cisco.com), as well as labs in [Cisco Modeling Labs (CML)]((https://github.com/xanderstevenson/data-center-development/tree/main/cml)). We've included sections here about setting up CML, as well as setting up [ProxMox](https://github.com/xanderstevenson/data-center-development/tree/main/proxmox) to host CML as a virtual machine.

<br>

### Table of Directories

- [Application Centric Infrastructure (ACI)](https://github.com/xanderstevenson/data-center-development/tree/main/aci): ACI Data Center development.

- [Cisco Modeling Labs (CML)](https://github.com/xanderstevenson/data-center-development/tree/main/cml) - How to install CML. Each section also contains info about how to using CML for the tools in that section.

- [Intersight](https://github.com/xanderstevenson/data-center-development/tree/main/intersight): automate Cisco Intersight.

- [Nexus Dashboard Facbric Controller (NDFC)](https://github.com/CiscoDevNet/data-center-development/tree/main/ndfc): automate NDFC, which is the successor to Cisco Data Center Network Manager (DCNM).

- [NX-OS](https://github.com/xanderstevenson/data-center-development/tree/main/nx-os/terraform_nx-os): NX-OS Data Center Development. We have sections for automating NX-OS with Ansible, Python Scripting, and Terraform, as well as how to use Splunk Telemetry with NX-OS.

- [Proxmox Setup Guide](https://github.com/xanderstevenson/data-center-development/edit/main/proxmox/README.md): This guide will help you set up Proxmox on both a laptop and a MiniPC. We also cover steps for Mac, Windows, and Linux.


<br>


## Installation

Clone the main repo (if you haven't already done so).

```bash
git clone https://github.com/xanderstevenson/data-center-development.git
cd data-center-development
```
<br>

### Create and activate a Python virtual environment

- Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
- Windows
```bash
python3 -m venv venv
venv\Scripts\activate
```
<br>

### Install dependencies

```bash
pip install -r requirements.txt
```
<br>


## Usage

Each section will have specific instructions on how to run code. For example, in the nx-os/ansible_nx-os section, each playbook is listed in the README, along with a copy/pastable command for running it, e.g.

- Name: `backup_config.yaml`
  - Purpose: Backup the current configuration of NX-OS devices
  - How to run:

    ```bash
    ansible-playbook playbooks/backup_config.yaml
    ```
  <br>
