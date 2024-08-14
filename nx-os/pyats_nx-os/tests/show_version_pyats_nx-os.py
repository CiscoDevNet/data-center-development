from pyats.topology import loader
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load the testbed file
testbed = loader.load("testbed.yaml")

# Access the device
device = testbed.devices["Nexus9k"]

# Connect to the device
device.connect()

# Execute a command
output = device.execute("show version")

# Print the output
print(output)
