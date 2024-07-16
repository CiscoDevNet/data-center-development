# Automate Cisco ACI with Ansible

Ansible ACI Modules: Use the Cisco ACI collection of Ansible modules to automate tasks. These modules cover various ACI functionalities such as tenant, application profile, endpoint group (EPG), and more.
Playbooks: Write Ansible playbooks to manage your ACI environment. Examples include creating tenants, configuring networks, and deploying policies.

`[Instructions for cloning this repo and installing the dependencies](https://github.com/xanderstevenson/data-center-development/blob/main/README.md) can be found on the [landing page for this repo.`

- Change directories

```
cd data-center-development/aci/ansible_aci
```


- Install The Cisco ACI collection of nodules from Asnible Galaxy

```
ansible-galaxy collection install cisco.aci
```

