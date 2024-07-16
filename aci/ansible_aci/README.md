# Automate Cisco ACI with Ansible

## Overview

**Ansible ACI Modules**: Use the Cisco ACI collection of Ansible modules to automate tasks. These modules cover various ACI functionalities such as tenant, application profile, endpoint group (EPG), and more.

**Playbooks**: Write Ansible playbooks to manage your ACI environment. Examples include creating tenants, configuring networks, and deploying policies.

**Fabric to Manage**: We will be utilizing the [ACI Simulator Always-On sandbox](https://devnetsandbox.cisco.com/DevNet/catalog/Open-NX-OS-Programmability_open-nx-os) from Cisco DevNet. If you use a different fabric, merely change the ansible host and credentials in the Ansible Vault. See Installation section below for details on setting up the Ansible Vault.


*[Instructions for cloning this repo and installing the dependencies](https://github.com/xanderstevenson/data-center-development/blob/main/README.md) can be found on the landing page for this repo.*

<br>

## Installation


- Change directories

```bash
cd data-center-development/aci/ansible_aci
```


- Install The Cisco ACI collection of nodules from Asnible Galaxy

```bash
ansible-galaxy collection install cisco.aci
```


- Set up the Ansible Vault

```bash
ansible-vault create vault.yaml
```

This command will open your default text editor (e.g., vi or nano), where you can input the sensitive information. After saving and closing the editor, the file will be encrypted.

Here's what mine looks like for the ACI Simulator Always-On sandbox:

```bash
ansible_user: admin
ansible_password: !v3G@!4@Y

```

If you want to edit the vault file later, use the ansible-vault edit command:

```bash
ansible-vault edit vault.yaml
```


<br>

## Usage

Because we added our credentials to Ansible Vault during the installation, we should be sure to invoke the vault when running our playbooks, for example:

```bash
ansible-playbook -i inventory.yml playbook.yml --ask-vault-pass
```


