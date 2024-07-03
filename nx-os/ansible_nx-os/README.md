# Ansible and NX-OS

## Overview 

This section details how to use Ansible to configure and interact with a Nexus 9000-series switch running NX-OS.

In the NX-OS section we discuss using Cisco Modeling Labs to host a lab with a nxos9000 node and that is what I'll be using in this section


## Prerequisites

- You should have an enviornment with an NX-OS 9000-series switch running NX-OS. You should be able to ping that device and enter it via SSH.
- OS: Mac, Windows, Linux should all be fine
- Web browser
- IDE - [Visual Studio Code](https://code.visualstudio.com/Download) recommended
- [Python](https://www.python.org/downloads/) 3.8 or higher installed (tested on Python 3.10.14 and 3.11.9)
- Ansible installed

## Environment Setup

Before diving into each section, clone the main repo and change directories to this point.

```bash
git clone
cd
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


## Playbooks



- Name: banner.yaml

- Purpose: Set the Exec and MOTD banners on NX-OS

- How to run:

```bash
ansible-playbook -i hosts playbooks/banner.yaml
```

- Result:

banner image

<br>



