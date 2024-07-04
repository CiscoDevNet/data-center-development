# NX-OS Data Center Development

## Overview 

This is the launch page for thr NX-OS section of Data Center Development. I've included the prerequisites and a CML Lab Setup section below to get you started before you explore the labs and their directories in this repo.


## Prerequisites

- You should have an enviornment with an NX-OS 9000-series switch running NX-OS.
- An IDE (e.g. VS Code)


## CML Lab Setup

I'm using Cisco Modeling Labs v2.6.1 running as a VM in ProxMox. As described in the CML section of this repo, I have an external connectior in bridge mode with an unmanaged switch attached to it. To this unmanaged switch, I've added a NX-OS 9000 node.

An NX-OS node in CML requires *GB (8192 MiB) of DRAM and 2 vCPUs

![Alt text]([URL](https://github.com/xanderstevenson/data-center-development/blob/main/nx-os/images/nx-os_node_setup.png?raw=true))


I've added a link from port 1 on the unmanaged switch to Ethernet1/1 on the NX-OS

Then, I just added these basic settings for Ethernet1/1 so I can connect with my laptop on my local 192.168.254.0 network:

login: admin
password: cisco

terminal length 0
no debug all

conf t
    hostname Nexus9k

interface Ethernet1/1
    no switch port
    ip address 192.168.254.101/24
    no shutdown
    ping 192.168.254.65

```
Nexus9k(config-if)# ping 192.168.254.65
PING 192.168.254.65 (192.168.254.65): 56 data bytes
64 bytes from 192.168.254.65: icmp_seq=0 ttl=63 time=4.895 ms
64 bytes from 192.168.254.65: icmp_seq=1 ttl=63 time=4.403 ms
64 bytes from 192.168.254.65: icmp_seq=2 ttl=63 time=3.01 ms
64 bytes from 192.168.254.65: icmp_seq=3 ttl=63 time=2.959 ms
64 bytes from 192.168.254.65: icmp_seq=4 ttl=63 time=2.86 ms
--- 192.168.254.65 ping statistics ---
5 packets transmitted, 5 packets received, 0.00% packet loss
round-trip min/avg/max = 2.86/3.625/4.895 ms
```

    exit
exit
copy running-config startup-config 


To confirm connectivity, you should not only be able to ping from the NX-OS node to your local network, but in the other direction as well.

In addition, make sure you can SSH from your local device to the NX-OS node.

```
ssh admin@192.168.254.101
The authenticity of host '192.168.254.101 (192.168.254.101)' can't be established.
RSA key fingerprint is SHA256:******************************.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.254.101' (RSA) to the list of known hosts.
User Access Verification
(admin@192.168.254.101) Password: 

Cisco NX-OS Software
Copyright (c) 2002-2022, Cisco Systems, Inc. All rights reserved.
Nexus 9000v software ("Nexus 9000v Software") and related documentation, files or other reference materials ("Documentation") are the proprietary property and confidential information of Cisco Systems, Inc. ("Cisco") and are protected, without limitation, pursuant to United States and International copyright and trademark laws in the applicable jurisdiction which provide civil and criminal penalties for copying or distribution without Cisco's authorization.

Any use or disclosure, in whole or in part, of the Nexus 9000v Software or Documentation to any third party for any purposes is expressly prohibited except as otherwise authorized by Cisco in writing. The copyrights to certain works contained herein are owned by other third parties and are used and distributed under license. Some parts of this software may be covered under the GNU Public License or the GNU Lesser General Public License. A copy of each such license is available at
http://www.gnu.org/licenses/gpl.html and
http://www.gnu.org/licenses/lgpl.html
***************************************************************
Nexus9k# 
```

## Next Steps

Once you've stablished connectivity between your local system and the Nexus 9k, you can proceed to the labs in this directory.
