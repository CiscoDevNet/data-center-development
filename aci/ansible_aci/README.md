Ansible

Ansible ACI Modules: Use the Cisco ACI collection of Ansible modules to automate tasks. These modules cover various ACI functionalities such as tenant, application profile, endpoint group (EPG), and more.
Playbooks: Write Ansible playbooks to manage your ACI environment. Examples include creating tenants, configuring networks, and deploying policies.

Example Ansible Playbook:


- name: Configure ACI Tenant
  hosts: aci
  gather_facts: no
  tasks:
    - name: Create a tenant
      cisco.aci.aci_tenant:
        host: "{{ inventory_hostname }}"
        username: "{{ aci_username }}"
        password: "{{ aci_password }}"
        tenant: "example_tenant"
        state: present
