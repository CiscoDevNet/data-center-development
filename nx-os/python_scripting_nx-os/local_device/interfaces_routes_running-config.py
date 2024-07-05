import subprocess
import re
import datetime

def run_cli_command(command):
    try:
        process = subprocess.Popen(f"ssh -i ~/.ssh/id_rsa {username}@{host} \"{command}\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
        print(f"Error saving to file {filename}: {e}")

if __name__ == "__main__":
    # Read inventory file for host, username, password
    with open("inventory.txt", "r") as inventory_file:
        host, username, password = inventory_file.read().strip().split(",")
    
    # Example commands
    commands = [
        "show interface brief",
        "show ip route",
        "show running-config"
    ]
    
    folder_name = "interfaces_routes_running-config"
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Create folder if it doesn't exist
    try:
        subprocess.run(f"mkdir {folder_name}", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        if e.returncode == 1:  # Folder already exists
            pass
        else:
            print(f"Error creating folder: {e}")
            exit(1)
    
    for command in commands:
        command_output = run_cli_command(command)
        if command_output:
            print(f"Command '{command}' output:")
            print(command_output)
            print("\n")
            
            # Save output to file with timestamp
            filename = f"{folder_name}/interfaces_routes_running-config_{timestamp}.txt"
            save_to_file(filename, command_output)
