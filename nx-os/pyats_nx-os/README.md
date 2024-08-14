<h1 align="center">Automating NX-OS with pyATS</h1>
<p align="center">
<img src="https://github.com/user-attachments/assets/80fc22dc-5b7a-4bc7-9690-a58c6a4a002e" width="200">
</p>


## Overview 

Here you will find a a pyATS (Python Automated Test Systems) testbed and tests to run automation against NX-OS. 

pyATS is a powerful framework developed by Cisco Systems designed to automate the testing and validation of network devices and infrastructure. Released in 2017, pyATS aims to simplify and streamline network testing through Python-based automation. The framework provides tools and libraries for creating, managing, and executing automated tests, particularly in network environments, where it can handle device configuration, performance, and functionality tests.

I'm utlizing NX-OS running on a local instance of CML as described [here](https://github.com/CiscoDevNet/data-center-development/tree/main/nx-os#user-content-lab-setup-adding-an-nx-os-9000-node-in-cisco-modeling-labs)



<br>

## Setup

### Export the NX-OS credentials so they can be used by the testbed.

We are using the default credentials for NX-OS in CML (admin/cisco) and managing the password with pyATS Secret Strings, described in the section below. Credentials can also be managed with Ansible Vault or other secrets managers such as HashiCorp Vault, AWS Secrets Manager, or Azure Key Vault.

<br>

## Secret Strings

"To address these security concerns, pyATS introduces the concept of "secret strings"
as a robust mechanism for safeguarding sensitive data. Secret strings are built in pyATS
functionality. This feature allows users to encrypt specific variables within the testbed.
yaml file, or even the entire file itself, thereby securing the credentials and other sensitive
information contained within. The encryption process ensures that even if the testbed
file is inadvertently exposed or accessed by unauthorized individuals, the encrypted contents
remain protected, thus maintaining the integrity and security of the network testing
environment. This approach not only reinforces the security posture of the testing framework
but also aligns with best practices for handling sensitive information in network
automation tasks." - [Cisco pyATS Network Test and Automation Solution: Data-driven and reusable testing for modern networks](https://www.ciscopress.com/store/cisco-pyats-network-test-and-automation-solution-data-9780138031671) - *a comprehensive book by our friends John Capobianco and Dan Wade.*

You can find information about using pyATS Secret Strings here: https://pubhub.devnetcloud.com/media/pyats/docs/cli/pyats_secret.html#pyats-secret

However, the best walkthrough we've seen regarding pyATS Secret Strings is in Appendix B of the pyATS book mentioned above.


<br>

## Running the pyATS tests

Tests are run from this directory as such:

```bash
python3 tests/show_version_pyats_nx-os.py     
```

<br>

## The pyATS Tests


1. show_version_pyats_nx-os - shows the version information


2. interface_collector_pyats_nx-os.py - provides a structured (JSON) summary of interface information for each device in the testbed. It includes details such as: Interface Name, IP address, Status, Protocol, and Additional Fields: Depending on the command, it might also include VLAN, duplex settings, and speed for interfaces.

<br>

## pyATS Resources

- [Cisco pyATS: Network Test & Automation Solution](https://developer.cisco.com/docs/pyats/) on Cisco DevNet.

- [Cisco pyATS Network Test and Automation Solution: Data-driven and reusable testing for modern networks](https://www.ciscopress.com/store/cisco-pyats-network-test-and-automation-solution-data-9780138031671) - a comprehensive book by our friendsJohn Capobianco and Dan Wade.

