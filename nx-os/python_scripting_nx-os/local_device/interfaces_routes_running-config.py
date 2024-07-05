import subprocess
from datetime import datetime

def run_cli_command(command):
    try:
        process = subprocess.Popen(f"dohost \"{command}\"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            raise Exception(stderr.decode("utf-8").strip())
        return stdout.decode("utf-8").strip()
    except Exception as e:
        print(f"Error running CLI command '{command}': {e}")
        return None

def save_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

if __name__ == "__main__":
    # Run commands to get interfaces, routes, and running config
    interface_output = run_cli_command("show interface")
    route_output = run_cli_command("show ip route")
    running_config_output = run_cli_command("show running-config")

    # Create folder if it doesn't exist
    folder_name = "/bootflash/scripts/interfaces_routes_running-config"
    subprocess.run(["mkdir", "-p", folder_name])

    # Save outputs to timestamped files
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    save_to_file(f"{folder_name}/interfaces_{timestamp}.txt", interface_output)
    save_to_file(f"{folder_name}/routes_{timestamp}.txt", route_output)
    save_to_file(f"{folder_name}/running-config_{timestamp}.txt", running_config_output)
