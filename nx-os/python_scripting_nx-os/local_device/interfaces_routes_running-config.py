import subprocess
from datetime import datetime
import os

def run_cli_command(command):
    try:
        process = subprocess.Popen(f"sshpass -p '{password}' ssh {username}@{host} \"{command}\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to {filename}: {e}")

if __name__ == "__main__":
    # Read inventory.txt for host, username, and password
    with open("inventory.txt", "r") as inventory_file:
        host, username, password = inventory_file.read().strip().split(",")

    # Create a timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # Create a folder to store results if it doesn't exist
    folder_name = f"interfaces_routes_running-config"
    os.makedirs(folder_name, exist_ok=True)

    # Run commands
    interface_output = run_cli_command("show interface brief")
    if interface_output:
        save_to_file(f"{folder_name}/interfaces_{timestamp}.txt", interface_output)

    route_output = run_cli_command("show ip route")
    if route_output:
        save_to_file(f"{folder_name}/routes_{timestamp}.txt", route_output)

    config_output = run_cli_command("show running-config")
    if config_output:
        save_to_file(f"{folder_name}/running-config_{timestamp}.txt", config_output)
