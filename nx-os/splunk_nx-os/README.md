# Splunk Telemetry and NX-OS

> **Note:** I wasn't able to install the Splunk Universal Forwarder in neither the Guestshell nor Bash on NX-OS running on Cisco Modeling Labs due to lack of disk space. However, I wanted to share this with you in case you have a non-CML instance of NX-OS you want to add Splunk Telemtery to.

Splunk is a web-based data collection, analysis, and monitoring tool. Splunk Enterprise helps
you gain valuable operational intelligence from your machine-generated data. It comes with a
full range of powerful search, visualization and pre-packaged content for use-cases where any
user can quickly discover and share insights. The raw data is sent to the Splunk server using the
Splunk Universal Forwarder. Universal Forwarders provide reliable and secure data collection
from remote sources while forwarding data into Splunk Enterprise for indexing and consolidation. 

A Splunk Enterprise infrastructure can scale to tens of thousands of remote systems, collecting terabytes of data with minimal impact on performance.

NX-OS with Splunk enables network operators to:

- Gain visibility into their infrastructure
- Track detailed network inventory
- Track power usage and temperature
- Authenticate and audit configuration changes
- Collect performance data from network devices

## Step 1

- Download Splunk Enterprise and the Universal Forwarder: https://www.splunk.com/en_us/download.html
- Choose the Splunk Enterprise version based on the OS of your control node
- Choose the version of Universal Forwarder based on the results of running `'show version' in NX-OS.
  
- Install Splunk Enterprise on your control node (I installed it on my laptop)

- Install the Universal Forwarder on the device running NX-OS. SCP and TFTP were not working so I ran an http server in my Downloads folder on my laptop and used cURL on NX-OS to receive the file:

On local device
```
Downloads % python3 -m http.server 8088
Serving HTTP on :: port 8088 (http://[::]:8088/) ...
```

On NX-OS in GuestShell
```
curl -O http://<insert-local-ip>/splunkforwarder-<insert-you-file>.tgz
```

- Note: to only place with enough space to install the forwarder in the GuestShell was in /bootflash. This command was necessary to extract it:

```
tar -xzpf splunkforwarder-9.2.2-d76edf6f0a15-Linux-x86_64.tgz --no-same-owner --no-same-permissions
```

- Follow Steps here: https://docs.splunk.com/Documentation/Forwarder/9.2.2/Forwarder/Installanixuniversalforwarder

<br>

## Resources

Use Splunk to gain visibility into infrastructure, track inventory and power usage, authenticate and audit configuration changes, and collect performance data from network devices.

**Download Free Trials of Splunk Cloud Platform and Splunk Enterprise**
https://www.splunk.com/en_us/download.html/



