<h1 align="center">Proxmox Setup Guide</h1>

This guide will help you set up Proxmox on both a laptop and a MiniPC. We will cover steps for Mac, Windows, and Linux.

## Table of Contents

1. [Requirements](#requirements)
2. [Creating a Proxmox Installation USB](#creating-a-proxmox-installation-usb)
    - [Mac](#mac)
    - [Windows](#windows)
    - [Linux](#linux)
3. [Installing Proxmox](#installing-proxmox)
4. [Initial Configuration](#initial-configuration)
5. [Accessing Proxmox GUI](#accessing-proxmox-gui)

## Requirements

- A USB drive with at least 2GB of storage.
- Proxmox VE ISO image. Download it from [Proxmox Download Page](https://www.proxmox.com/en/downloads).
- A laptop or MiniPC for the installation.

## Creating a Proxmox Installation USB

### Mac

1. **Download and Install Etcher:**
   - Download Etcher from [balena.io](https://www.balena.io/etcher/).
   - Install Etcher by opening the downloaded `.dmg` file and dragging Etcher to the Applications folder.

2. **Create Bootable USB:**
   - Open Etcher.
   - Select the Proxmox VE ISO file.
   - Select your USB drive.
   - Click "Flash" to create the bootable USB.

### Windows

1. **Download and Install Rufus:**
   - Download Rufus from [rufus.ie](https://rufus.ie/).
   - Install Rufus by running the downloaded `.exe` file.

2. **Create Bootable USB:**
   - Open Rufus.
   - Select your USB drive under "Device".
   - Select the Proxmox VE ISO file under "Boot selection".
   - Click "Start" to create the bootable USB.

### Linux

1. **Install Etcher:**
   - Download Etcher from [balena.io](https://www.balena.io/etcher/).
   - Follow the installation instructions for your Linux distribution.

2. **Create Bootable USB:**
   - Open Etcher.
   - Select the Proxmox VE ISO file.
   - Select your USB drive.
   - Click "Flash" to create the bootable USB.

## Installing Proxmox

1. **Boot from USB:**
   - Insert the USB drive into your laptop or MiniPC.
   - Boot the system and enter the BIOS/UEFI settings (usually by pressing F2, F12, DEL, or ESC during startup).
   - Set the USB drive as the primary boot device and save the changes.

2. **Install Proxmox:**
   - Follow the on-screen instructions to install Proxmox VE.
   - Select the target hard drive, time zone, and create a password for the root user.

## Initial Configuration

1. **Network Configuration:**
   - During the installation, configure the network settings.
   - Set the IP address, gateway, and DNS servers for your Proxmox server.

2. **Finish Installation:**
   - Complete the installation process and remove the USB drive.
   - Reboot the system.

## Accessing Proxmox GUI

1. **Connect to Proxmox:**
   - Open a web browser on your computer.
   - Enter the IP address of your Proxmox server followed by `:8006` (e.g., `https://192.168.1.100:8006`).

2. **Login to Proxmox:**
   - Use the `root` user and the password you created during the installation.
   - You can now start creating virtual machines and managing your Proxmox server.

## Additional Resources

- [Proxmox Documentation](https://pve.proxmox.com/wiki/Main_Page)
- [Proxmox Community Forum](https://forum.proxmox.com/)
- [Proxmox YouTube Channel](https://www.youtube.com/user/ProxmoxVE)

This guide provides a basic overview of installing Proxmox on a laptop or MiniPC. For advanced configurations and troubleshooting, refer to the Proxmox documentation and community resources.
