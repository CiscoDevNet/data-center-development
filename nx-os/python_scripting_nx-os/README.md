# Python Scripting for NX-OS

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

<br>

### On-Device scripts

These devices are designed to run within the Guest Shell of a Cisco NX-OS device. Therefore, after making sure guestshell is enabled, you will enter the NX-OS GuestShell and **paste in the entire contents of the script found in this directoy --- into the /bootflash/scripts directory in the guestshell on NX-OS --- and you will then hit ENTER**. We place scripts there because that dir will be persistent across reboots of the device.

```bash
guestshell enable
guestshell
cd /bootflash/scripts
```
<br>


#### Different ways to schedule and run the on-device Python scripts:

To schedule and run the nxos_resources.py script on Cisco NX-OS, you have several options depending on where you want to execute it from (Guest Shell, Bash, NX-CLI, or externally via API/cURL). Below are the different methods:

1. From within the Guest Shell (Cron Job)
You can use cron in the Guest Shell to schedule the script:

Open the crontab file for editing:
```crontab -e```
Add a cron job entry to schedule the script (e.g., to run every hour):
0 * * * * /usr/bin/python /bootflash/scripts/nxos_resources.py
<br>

2. From Bash (Manual Execution or Script)
You can manually execute the script or include it in another Bash script:

Manual execution:
```python /bootflash/scripts/nxos_resources.py```
Include in another script:
```#!/bin/bash
python /bootflash/scripts/nxos_resources.py```
Then make your script executable and run it:
```chmod +x your_script.sh
./your_script.sh```
<br>

3. From NX-CLI (EEM Script)
You can use Embedded Event Manager (EEM) to run the script:

Create an EEM applet:
```
event manager applet RunScript
event timer cron cron-entry "0 * * * *"
action 1.0 cli command "guestshell run python /bootflash/scripts/nxos_resources.py"```
<br>

4. From Outside via API/cURL
You can use the NX-API to execute CLI commands remotely, including running the script:

Enable NX-API on the device:

```feature nxapi```
Use cURL to invoke the script:
```curl -X POST -d '{"ins_api": {"version": "1.0", "type": "cli_show", "chunk": "0", "sid": "1", "input": "guestshell run python /bootflash/scripts/nxos_resources.py", "output_format": "json"}}' http://<nxos_device_ip>/ins -u <username>:<password> -H "Content-Type: application/json"```
<br>

5. From an External Scheduler (e.g., a remote server using SSH)
You can use a remote scheduler or cron job on another machine to SSH into the NX-OS device and run the script:
```crontab -e```
Add an entry to SSH into the NX-OS device and run the script (e.g., every hour):
```0 * * * * ssh user@nxos_device 'guestshell run python /bootflash/scripts/nxos_resources.py'```

Each method has its own use case, whether you need the script to run locally within the NX-OS environment or remotely from an external system.```
<br>

#### List of On-Device scripts

**1. nxos_resources.py**

Description: When executed, the script will print the system's CPU information and the top 10 processes by memory usage. The output is formatted with separators for better readability.



