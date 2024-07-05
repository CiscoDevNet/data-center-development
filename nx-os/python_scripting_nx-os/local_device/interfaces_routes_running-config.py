import paramiko
from datetime import datetime

# Configuration for your NX-OS device
HOST = 'your_device_ip_or_hostname'
USERNAME = 'your_username'
PASSWORD = 'your_password'
PORT = 22  # SSH port

def run_cli_command_ssh(command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(HOST, port=PORT, username=USERNAME, password=PASSWORD, timeout=5)
        
        stdin, stdout, stderr = client.exec_command(command)
        stdout_str = stdout.read().decode('utf-8')
        stderr_str = stderr.read().decode('utf-8')
        
        if stderr_str:
            raise Exception(stderr_str.strip())
        
        return stdout_str.strip()
    
    except Exception as e:
        print(f"Error running CLI command '{command}': {e}")
        return None

def save_to_file(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(data)
        print(f"Saved data to {filename}")
    except Exception as e:
        print(f"Error saving to file {filename}: {e}")

if __name__ == "__main__":
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    folder_name = f"interfaces_routes_running-config"
    
    # Example NX-OS commands
    interface_command = "show interface brief"
    route_command = "show ip route"
    config_command = "show running-config"
    
    # Run commands via SSH
    interface_output = run_cli_command_ssh(interface_command)
    route_output = run_cli_command_ssh(route_command)
    config_output = run_cli_command_ssh(config_command)
    
    # Save outputs to files locally
    if interface_output:
        save_to_file(f"{folder_name}/interfaces_{timestamp}.txt", interface_output)
    
    if route_output:
        save_to_file(f"{folder_name}/routes_{timestamp}.txt", route_output)
    
    if config_output:
        save_to_file(f"{folder_name}/running-config_{timestamp}.txt", config_output)
