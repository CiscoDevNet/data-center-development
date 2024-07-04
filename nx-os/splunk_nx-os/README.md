# Splunk Telemetry and NX-OS

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

- Install the Universal Forwarder on the device running NX-OS



