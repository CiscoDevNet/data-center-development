import os
import paramiko
from datetime import datetime
import warnings

# Suppress all CryptographyDeprecationWarnings
warnings.filterwarnings("ignore", category=Warning)

# Function to execute commands on the device
def execute_command(ssh, command):
    stdin, stdout, stderr = ssh.exec_command(command)
    return stdout.read().decode()

# Function to capture output and save to file with timestamp
def capture_and_save(ssh, command, filename):
    output = execute_command(ssh, command)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    directory = "./interfaces_routes_running-config"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(f"{directory}/{filename}_{timestamp}.txt", 'w') as file:
        file.write(output)
    print(f"Captured {filename} at {timestamp}")

# Main script
# Read credentials and device from inventory.txt
with open('inventory.txt') as f:
    for line in f:
        # Skip empty lines or lines starting with '#' (comments)
        if line.strip() == '' or line.strip().startswith('#'):
            continue
        
        # Attempt to split line into device, username, and password
        try:
            device, username, password = line.strip().split(',')
        except ValueError:
            print(f"Skipping line: {line.strip()} - does not match expected format")
            continue
        
        # Establish SSH connection
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(device, username=username, password=password, allow_agent=False, look_for_keys=False)
            
            # Capture outputs
            capture_and_save(ssh, "show interface brief", "interface_brief")
            capture_and_save(ssh, "show ip route", "ip_route")
            capture_and_save(ssh, "show running-config", "running_config")
            
        except paramiko.AuthenticationException:
            print(f"Authentication failed for {device} with user {username}")
        except paramiko.SSHException as e:
            print(f"Failed to connect to {device}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Ensure the SSH connection is closed
            ssh.close()
