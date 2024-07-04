

## Overview

If you've taken out this learning lab I created on Cisco DevNet called 
[Automating Network Tasks with Cisco NX-OS Device-Level APIs](https://developer.cisco.com/learning/labs/dne-dci-nxos-device-level-apis/introduction/), 
you'll know that We can interact with NX-OS using Python in basically four different ways:

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

3. Through either the Python2 or Python3 version installed in the GuestShell

```
nxos# guestshell
[admin@guestshell ~]$ python -V
Python 2.7.5
[admin@guestshell ~]$ python3 -V
Python 3.6.8
```
<br>

4. Through Python scripts that you run locally against the device running NX-OS. Two great ways to create such scripts are through the NX-API Sandbox and Postman,
5. both of which provide buttons for easily converting (API requests in the case of Postman and CLI commands or Data Models in the case of the NX-API Sandbox) into Python scripts.

6. 

