# Data Center Development


## Project Description

This is a repository for code and instructions to help you interact with and automate Cisco Data Center technologies, such as Nexus Switches, NX-OS, Application Centric Infrastructure (ACI), Unified Computing System (UCS), Instersight, and more.

The code in these directories was primarily tested against labs in Cisco Modeling Labs (CML), and we've included sections here about setting up CML, as well as setting up ProxMox to host CML as a virtual machine.

<br>

### Table of Directories

- [Cisco Modeling Labs (CML)](https://github.com/xanderstevenson/data-center-development/tree/main/nx-os/ansible_nx-os) - How to install CML. Each section also contains info about how to using CML for the tools in that section.

- [Proxmox Setup Guide](https://github.com/xanderstevenson/data-center-development/edit/main/proxmox/README.md): This guide will help you set up Proxmox on both a laptop and a MiniPC. We also cover steps for Mac, Windows, and Linux.

- [NX-OS](https://github.com/xanderstevenson/data-center-development/tree/main/nx-os/terraform_nx-os): NX-OS Data Center Development. We have sections for automating NX-OS with Ansible, Python Scripting, and Terraform, as well as how to use Splunk Telemetry with NX-OS.

- [Application Centric Infrastructure (ACI)](): ACI Data Center Development. Coming soon...


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
