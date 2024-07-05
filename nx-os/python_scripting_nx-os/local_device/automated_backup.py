import os
import datetime
import paramiko
from paramiko import SSHClient, AutoAddPolicy

# Function to read credentials from inventory.txt
def read_credentials(file_path):
    credentials = {}
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():  # Ignore empty lines
                ip, username, password = line.strip().split(',')
                credentials[ip] = {'username': username, 'password': password}
    return credentials

# Function to connect to device and run commands
def ssh_command(ip, username, password, commands):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(ip, username=username, password=password, allow_agent=False, look_for_keys=False)

    outputs = {}
    for command in commands:
        stdin, stdout, stderr = client.exec_command(command)
        outputs[command] = stdout.read().decode()

    client.close()
    return outputs

# Function to save output to file
def save_to_file(ip, outputs):
    # Create directory if it doesn't exist
    directory = 'automated_backup'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create filename with timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'{directory}/{ip}_automated_backup_{timestamp}.txt'

    # Write each command's output to file
    with open(filename, 'w') as f:
        for command, output in outputs.items():
            f.write(f'===== {command} =====\n\n')
            f.write(output)
            f.write('\n\n')

# Main function
if __name__ == '__main__':
    # Path to the inventory.txt file
    inventory_file = 'inventory.txt'

    # Read credentials from inventory file
    credentials = read_credentials(inventory_file)

    # List of commands to execute
    commands = [
        'show running-config',
        'show logging',
        'show version'
    ]

    # Execute commands for each device
    for ip, cred in credentials.items():
        username = cred['username']
        password = cred['password']

        # Execute commands
        outputs = ssh_command(ip, username, password, commands)

        # Save outputs to file
        save_to_file(ip, outputs)

    print(f'Automated backup completed successfully for all devices.')
