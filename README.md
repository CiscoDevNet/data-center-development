# Data Center Development

# Project Description

This is a repository for code and instructions to help you interact with and automate Cisco Data Center technologies, such as Nexus Switches, NX-OS, Application Centric Infrastructure (ACI), Unified Computing System (UCS), Instersight, and more.

The code in these directories was primarily tested against labs in Cisco Modeling Labs (CML), and we've included sections here about setting up CML, as well as setting up ProxMox to host CML as a virtual machine.

## Installation

Before diving into each section, clone the main repo (if you haven't already done so).

```bash
git clone https://github.com/xanderstevenson/data-center-development.git
cd data-center-development
```
<br>

Create and activate a Python virtual environment

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

Install dependencies

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
