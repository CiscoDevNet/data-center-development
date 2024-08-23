# Data Center Development


## Project Description

This is a repository for code and instructions to help you interact with and automate Cisco Data Center technologies, such as [Data Center Switches](https://www.cisco.com/site/us/en/products/networking/cloud-networking-switches/index.html), [NX-OS](https://www.cisco.com/c/en/us/products/collateral/ios-nx-os-software/nx-os-software/data_sheet_c78-652063.html?dtid=osscdc000283), [Application Centric Infrastructure (ACI)](https://www.cisco.com/c/en/us/solutions/collateral/data-center-virtualization/application-centric-infrastructure/solution-overview-c22-741487.html), [Unified Computing System (UCS)](https://www.cisco.com/site/us/en/products/computing/servers-unified-computing-systems/index.html), [Instersight](https://intersight.com/), and more.

The code in these directories was primarily tested against the free [sandboxes from Cisco DevNet](https://devnetsandbox.cisco.com), as well as labs in Cisco Modeling Labs (CML). We've included sections here about setting up [CML](https://github.com/xanderstevenson/data-center-development/tree/main/cml), as well as setting up [ProxMox](https://github.com/xanderstevenson/data-center-development/tree/main/proxmox) to host CML as a virtual machine.

<br>

### Table of Directories

- [Application Centric Infrastructure (ACI)](https://github.com/xanderstevenson/data-center-development/tree/main/aci): ACI Data Center automation

- [Cisco Modeling Labs (CML)](https://github.com/xanderstevenson/data-center-development/tree/main/cml) - How to install CML. Each section also contains info about how to using CML for the tools in that section.

- [Intersight](https://github.com/xanderstevenson/data-center-development/tree/main/intersight): Automate Cisco Intersight
  
- [Proxmox Setup Guide](https://github.com/xanderstevenson/data-center-development/edit/main/proxmox/README.md): This guide will help you set up Proxmox on both a laptop and a MiniPC. We also cover steps for Mac, Windows, and Linux.

- [Nexus Dashboard Fabric Controller](https://github.com/CiscoDevNet/data-center-development/tree/main/ndfc): Automate VXLAN/EVPN fabrics.

- [NX-OS](https://github.com/xanderstevenson/data-center-development/tree/main/nx-os/terraform_nx-os): NX-OS Data Center Development.


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

## Infrastructure

The infrastructure we automate in this repo ranges from the free Cisco DevNet sandboxes (both always on and reservable), to dCloud pods, and Cisco Modeling Labs. So even if you don’t have physical access to an expensive data center, you can still learn, practice with, and grok these technologies.


<p align="center"><img src="https://github.com/user-attachments/assets/c82e4eaa-c085-4979-99c9-3e009ebfae0b" width="450"></p>

<br>

## Tools

The core tools to automate / orchestrate each Cisco Data Center product are Ansible, Python, and Terraform.

<p align="center"><img src="https://github.com/user-attachments/assets/ef8123e8-5b7a-460a-954a-ebe22e4188d1" width="450"></p>

<br>

However, some sections have additional tools shown for automation and orchestration of the product.

<p align="center"><img src="https://github.com/user-attachments/assets/5029325e-f8f3-41cc-b52c-decfd505d80c" width="450"></p>




