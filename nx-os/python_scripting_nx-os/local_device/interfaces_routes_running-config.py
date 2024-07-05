import subprocess
from datetime import datetime

def run_cli_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            raise Exception(stderr.decode("utf-8").strip())
        return stdout.decode("utf-8").strip()
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
    
    # Example commands, replace with actual commands for your devices
    interface_command = "show interface brief"
    route_command = "show ip route"
    config_command = "show running-config"

    # Run commands
    interface_output = run_cli_command(interface_command)
    route_output = run_cli_command(route_command)
    config_output = run_cli_command(config_command)

    # Save outputs to files locally
    if interface_output:
        save_to_file(f"{folder_name}/interfaces_{timestamp}.txt", interface_output)
    
    if route_output:
        save_to_file(f"{folder_name}/routes_{timestamp}.txt", route_output)
    
    if config_output:
        save_to_file(f"{folder_name}/running-config_{timestamp}.txt", config_output)
