# Ansible and NX-OS

## Overview 

This section details how to use Ansible to configure and interact with a Nexus 9000-series switch running NX-OS.

In the NX-OS section we discuss using Cisco Modeling Labs to host a lab with a nxos9000 node and that is what I'll be using in this section

<br>

## Prerequisites

- You should have an enviornment with an NX-OS 9000-series switch running NX-OS. You should be able to ping that device and enter it via SSH.
- OS: Mac, Windows, Linux should all be fine
- Web browser
- IDE - [Visual Studio Code](https://code.visualstudio.com/Download) recommended
- [Python](https://www.python.org/downloads/) 3.8 or higher installed (tested on Python 3.10.14 and 3.11.9)
- Ansible installed
<br>

## Environment Setup

### Before diving into each section, clone the main repo (if you haven't already done so) and change directories to this point.

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

### Change into the nx-os directory

```bash
cd nx-os/
```
<br>

### Add the IP or URL of your NX-OS device to the hosts inventory file.

<br>

### Export the Username and Password of your NX-OS device (for CML, its admin/cisco)

```bash
export NXOS_User=
export NXOS_Password=
```

<br>

## Playbooks

- Name: `banner.yaml`
  - Purpose: Set the Exec and MOTD banners on NX-OS
  - How to run:

    ```bash
    ansible-playbook playbooks/banner.yaml
    ```

  <br>

- Name: `backup_config.yaml`
  - Purpose: Backup the current configuration of NX-OS devices
  - How to run:

    ```bash
    ansible-playbook playbooks/backup_config.yaml
    ```
  <br>

- Name: `gather_facts.yaml`
  - Purpose: Gather facts from NX-OS devices
  - How to run:

    ```bash
    ansible-playbook playbooks/gather_facts.yaml
    ```

  <br>


- Name: `show_vdcs.yaml`
  - Purpose: Show VDCs on NX-OS devices
  - How to run:

    ```bash
    ansible-playbook playbooks/show_vdcs.yaml
    ```

  <br>

- Name: `configure_vlans.yaml`
  - Purpose: Configure VLANs on NX-OS devices
  - How to run:

    ```bash
    ansible-playbook playbooks/configure_vlans.yaml
    ```

  <br>

- Name: `show_vlans.yaml`
  - Purpose: Show VLANs on NX-OS devices
  - How to run:

    ```bash
    ansible-playbook playbooks/show_vlans.yaml
    ```

  <br>

- Name: `configure_vrfs.yaml`
  - Purpose: Configure VRFs on NX-OS devices
  - How to run:

    ```bash
    ansible-playbook playbooks/configure_vrfs.yaml
    ```

  <br>

- Name: `show_vrfs.yaml`
  - Purpose: Show VRFs on NX-OS devices
  - How to run:

    ```bash
    ansible-playbook playbooks/show_vrfs.yaml
    ```

  <br>





## Resources

- Cisco.Nxos Ansible Modules: https://docs.ansible.com/ansible/latest/collections/cisco/nxos/index.html

- ansible-nxos: https://github.com/Anyweb/ansible-nxos

- CiscoNXOSFacts: https://github.com/automateyournetwork/CiscoNXOSFacts/tree/main



