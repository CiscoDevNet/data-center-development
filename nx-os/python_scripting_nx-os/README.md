# Python Scripting for NX-OS

## Menu

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Environment Setup](#environment-setup)
    - [Clone Repository](#clone-repository)
    - [Create and Activate Python Virtual Environment](#create-and-activate-python-virtual-environment)
    - [Install Dependencies](#install-dependencies)
    - [Change into the python_scripting_nx-os Directory](#change-into-the-python_scripting_nx-os-directory)
    - [Export Environmental Variables](#export-environmental-variables)
4. [Usage](#usage)
    - [On-Device Scripts](#on-device-scripts)
        - [Different Ways to Schedule and Run On-Device Python Scripts](#different-ways-to-schedule-and-run-on-device-python-scripts)
    - [List of On-Device Scripts](#list-of-on-device-scripts)
    - [Local Scripts](#local-scripts)
    - [List of Local Scripts](#list-of-local-scripts)


## Overview

If you've taken out this learning lab I created on Cisco DevNet called 
[Automating Network Tasks with Cisco NX-OS Device-Level APIs](https://developer.cisco.com/learning/labs/dne-dci-nxos-device-level-apis/introduction/), 
you'll know that *we can interact with NX-OS using Python in basically **four** different ways*:


1. Through the one Python version installed on the device via the Python inerpreter by typing 'python' and entering commands lin-by-line (this is the most awkward/wonky option)

```
developer:src > python
Python 3.10.14 (main, Mar 23 2024, 12:43:01) [GCC 11.2.1 20220219] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
<br>

2. Through the one Python version installed on Bash within NX-OS

```
nxos# run bash
bash-4.4$ python -V
Python 3.8.14
```
<br>

3. Through either the Python2 or Python3 version installed in the GuestShell in NX-OS

```
nxos# guestshell
[admin@guestshell ~]$ python -V
Python 2.7.5
[admin@guestshell ~]$ python3 -V
Python 3.6.8
```
<br>

4. Through Python scripts that you run locally against the device running NX-OS. Two great ways to create such scripts are through the NX-API Sandbox and Postman,
both of which provide buttons for easily converting (API requests in the case of Postman and CLI commands or Data Models in the case of the NX-API Sandbox) into Python scripts.

<br>

## Prerequisites

- You should have an enviornment with an NX-OS 9000-series switch running NX-OS. You should be able to ping that device and enter it via SSH.
- OS: Mac, Windows, Linux should all be fine
- IDE - [Visual Studio Code](https://code.visualstudio.com/Download) recommended
- [Python](https://www.python.org/downloads/) 3 installed
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

### Change into the python_scripting_nx-os directory

```bash
cd nx-os/python_scripting_nx-os
```
<br>

### Export environmental variables

<br>

## Usage

Some of the scripts in the directory are meant to be run locally against a connected or remote device running NX-OS. Others are meant to be installed within NX-OS and run using Python from there. The scripts meant to be run from your local device are in the 'local_device' directory, while those meant to be run from *within* NX-OS are in the 'on_device' directory.

I've tested all scripts against NX-OS running on a Nexus 9000v switch in Cisco Modeling Labs.

<br>

### On-Device scripts

These scripts are designed to run within the Guest Shell of a Cisco NX-OS device. Therefore, after making sure guestshell is enabled, you will enter the NX-OS GuestShell. A simple way to add the script to the NX-OS GuestShell is paste or cat the script **into the /bootflash/scripts directory in the guestshell on NX-OS**. We place scripts there because that dir will be persistent across reboots of the device. You want to add the script there in other ways, such as SCP and TFTP.

```bash
guestshell enable
guestshell
cd /bootflash/scripts
```
<br>


#### Different ways to schedule and run the on-device Python scripts:

To schedule and run the nxos_resources.py script on Cisco NX-OS, you have several options depending on where you want to execute it from (Guest Shell, Bash, NX-CLI, or externally via API/cURL). Below are the different methods: 

<br>

**1. From within the Guest Shell (Cron Job)**

You can use cron in the Guest Shell to schedule the script:

Open the crontab file for editing:

```crontab -e```

Add a cron job entry to schedule the script (e.g., to run every hour):

```0 * * * * /usr/bin/python /bootflash/scripts/nxos_resources.py```
<br><br>
<br>

**2. From Bash (Manual Execution or Script)**
   
You can manually execute the script or include it in another Bash script:

Manual execution:
```python /bootflash/scripts/nxos_resources.py```

Include in another script:

```
#!/bin/bash
python /bootflash/scripts/nxos_resources.py
```

Then make your script executable and run it:

```
chmod +x your_script.sh
./your_script.sh
```
<br><br>

**3. From NX-CLI (EEM Script)**
You can use Embedded Event Manager (EEM) to run the script:

Create an EEM applet:

```
event manager applet RunScript
event timer cron cron-entry "0 * * * *"
action 1.0 cli command "guestshell run python /bootflash/scripts/nxos_resources.py"
```
<br><br>

**4. From Outside via API/cURL**
You can use the NX-API to execute CLI commands remotely, including running the script:

Enable NX-API on the device:

```feature nxapi```

Use cURL to invoke the script:

```
curl -X POST -d '{"ins_api": {"version": "1.0", "type": "cli_show", "chunk": "0", "sid": "1", "input": "guestshell run python /bootflash/scripts/nxos_resources.py", "output_format": "json"}}' http://<nxos_device_ip>/ins -u <username>:<password> -H "Content-Type: application/json"
```
<br>
<br>

**5. From an External Scheduler (e.g., a remote server using SSH)**
   
You can use a remote scheduler or cron job on another machine to SSH into the NX-OS device and run the script:

```crontab -e```

Add an entry to SSH into the NX-OS device and run the script (e.g., every hour):

```0 * * * * ssh user@nxos_device 'guestshell run python /bootflash/scripts/nxos_resources.py'```

<br>

Each method has its own use case, whether you need the script to run locally within the NX-OS environment or remotely from an external system.
<br>
<br>

#### List of On-Device scripts
<hr>

**1. nxos_resources.py**

When executed, the script will print the system's CPU information and the top 10 processes by memory usage. The output is formatted with separators for better readability.

<br>

**2. arp_exporter_nx-os.py**

Export the ARP table periodically to a CSV file for easier analysis.

<br>

**3. config_backup_nx-os.py**

Automatically back up the running configuration to a file or remote server.

<br>

**4. interface_status_nx-os.py**

Monitor the status of network interfaces and generate alerts or logs when an interface goes down.

<br>

**5. inventory_nx-os.py**

Gather and log inventory details such as module type, serial numbers, and software versions.

<br>

**6. syslog_alert_nx-os.py**

Monitor syslog messages for specific events and send alerts.


<br>

### Local scripts

These scripts are designed to run from your local device, such as a laptop, desktop, server, or control node. 

- You must create an inventory.txt file and place it in the same directory from which you will run these scripts. Here is the format of inventory.txt:

```
192.168.254.101,admin,cisco
```

> **Important** You will want to have a .gitignore file in the same directory inventory.txt is in, which list that file, in the case you want to push the script to a GitHub repo. Including usernames/passwords in inventory files is not the best practice, but it is better than hard coding them in the script if we can at least obfuscate them with .gitignore

<br>

-Python3 must be installed in order to run them. All libraries needed to run them should be either included in the Python standard library or installed from the [requirements.txt](https://github.com/xanderstevenson/data-center-development/blob/main/requirements.txt) file found at the root of this repo, like so:

```bash
pip install -r requirements.txt
```
<br>


- Then simply navigate to your local clone of this repo and change into the directory [nx-os/python_scripting_nx-os/local_device](https://github.com/xanderstevenson/data-center-development/tree/main/nx-os/python_scripting_nx-os/local_device)

From there, run the script of your choice like so:

```bash
python3 example_script.py
```

<br>
<br>

#### List of Local scripts
<hr>

**1. interfaces_routes_running-config.py**

For each device listed in inventory.txt, it executes three commands (show interface brief, show ip route, show running-config) to gather network interface status, IP routing information, and the current running configuration. The script captures the output of each command and saves it to timestamped text files (interface_brief_YYYY-MM-DD_HH-MM-SS.txt, ip_route_YYYY-MM-DD_HH-MM-SS.txt, running_config_YYYY-MM-DD_HH-MM-SS.txt) within a directory named interfaces_routes_running-config.

<br>

**2. automated_backup.py**

This Python script automates the backup process for network devices specified in an inventory.txt file. It connects to each device using SSH, retrieves the show running-config, show log, and show version outputs, and saves them into timestamped text files within an automated_backup directory. It first reads device credentials from the inventory.txt, establishes SSH connections using Paramiko, executes the commands, captures their outputs, and organizes them neatly into labeled sections within each backup file.





