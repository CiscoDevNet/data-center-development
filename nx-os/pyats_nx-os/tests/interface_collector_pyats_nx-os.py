from pyats.topology import loader
import logging
import json
import re

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load the testbed file
testbed = loader.load("testbed.yaml")


# Define a function to extract relevant interface information from command output
def parse_interface_output(command_output):
    interfaces_info = []

    if "show ip interface brief" in command_output:
        for line in command_output.splitlines():
            if re.match(r"\S+ \d+ \S+ \S+ \S+ \S+ \S+", line):
                parts = line.split()
                interface_info = {
                    "Interface": parts[0],
                    "IP Address": parts[1],
                    "Status": parts[4],
                    "Protocol": parts[5],
                }
                interfaces_info.append(interface_info)
    elif "show interface status" in command_output:
        for line in command_output.splitlines():
            if re.match(r"\S+ \d+ \S+ \S+ \S+ \S+", line):
                parts = line.split()
                interface_info = {
                    "Interface": parts[0],
                    "Status": parts[1],
                    "VLAN": parts[2],
                    "Duplex": parts[3],
                    "Speed": parts[4],
                }
                interfaces_info.append(interface_info)
    elif "show interface" in command_output:
        interface_blocks = re.split(r"\n(?=Ethernet\d+/\d+)", command_output.strip())
        for block in interface_blocks:
            interface_name = re.search(r"^(Ethernet\d+/\d+)", block)
            link_status = re.search(r"is (\w+)", block)
            admin_state = re.search(r"admin state is (\w+)", block)
            ip_address = re.search(r"Internet address is (\S+)", block)

            if interface_name:
                interface_info = {
                    "Interface": interface_name.group(1),
                    "Link Status": link_status.group(1) if link_status else "N/A",
                    "Admin State": admin_state.group(1) if admin_state else "N/A",
                    "IP Address": ip_address.group(1) if ip_address else "N/A",
                }
                interfaces_info.append(interface_info)

    return interfaces_info


# Define a function to collect device interface information
def collect_device_info(device):
    try:
        # Connect to the device
        device.connect()

        # Define commands to gather interface information
        commands = [
            "show ip interface brief",
            "show interface status",
            "show interface",
        ]

        results = {}
        for command in commands:
            try:
                output = device.execute(command)
                # Process command output to extract relevant information
                results[command] = parse_interface_output(output)
            except Exception as e:
                logging.error(f"Error executing command '{command}': {e}")

        return results

    except Exception as e:
        logging.error(f"Error connecting to {device.name}: {e}")
        return None


# Access devices and collect information
results = {}
for device_name in testbed.devices:
    device = testbed.devices[device_name]
    results[device_name] = collect_device_info(device)

# Print results as JSON
print(json.dumps(results, indent=4))
