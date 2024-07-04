# Cisco Modeling Labs (CML)

CML is used extensively in this rep. I've added thi section to explain how I added CML as a VM to ProxMox.
For info on ProxMox see the proxmox directory in this repo. I've also included some links to CML resources.

<br>

## Installing CML as a VM in ProxMox

Once you have your CML license, you can go ahead and provision it as a VM in ProxMox.

- Within ProxMox, click ‘Create a VM’. The setting you use are pretty standard as compared to other VMs. I lef tthe default for most settings.

- Here are some setting which are peculiar to CML and must be set:

**OS tab**

Choose Use CD/DVD disk image file
for ISO image, choose the CML ISO you’ve uploaded to var/lib/vz/template/iso/ on your ProxMox server.
Choose Linux, and the latest version

**System tab**

q35 for Machine
OVMP (UEFI) for BIOS

**Disks tab**

Disk size 64GB

**CPU tab**

4Cores
I use 5

**Memory tab**

At least 8GB (8192 MiB)
I use 16 (16284 MiB)

<br>

- After that, start the CML VM, if you didn’t choose for it to automatically start. CML will walk you through the installation. You’ll choose a username and password and will probably be warned this is a standalone installation, which is fine.

- The only issue I had with the installation was a warning that virtualization was disabled. I knew this was not true because I already had other VMs running on ProxMox but I double checked the BIOS on my MiniPC running ProxMox. What I ended up having to do was change the ‘cpu’ name to ‘host’ on the config file for the CML VM. It was located at /etc/pve/qemu-server/102.conf. If that doesn’t fix it, enable nested virtualization on your ProxMox server.

- Once CML loads successfully and passes all tests, you can upload the Refplat ISO through the cml-controller dashboard. This will give you access to various types of nodes and schemas. Be sure to activate your license. 

- Now you can start your first lab.

- First Steps: Create an external connector node, set it in ‘bridge mode’, and start it. Then create an unmanaged switch, start it, and connect it to the external connector. Now you're ready to add nodes like routers and switches!

<br>

## CML Resources

[Introduction to Network Simulations with Cisco Modeling Labs | CMLLAB](https://u.cisco.com/paths/243) on Cisco U.

Gain an introductory understanding of the Cisco network simulation tool, Cisco Modeling Labs.
