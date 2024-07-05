import subprocess
import os
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

if __name__ == "__main__":
    config_output = run_cli_command("show running-config")
    if config_output:
        # Create the directory if it doesn't exist
        logs_dir = "/bootflash/scripts/config-backups"
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        # Define the file path
        file_path = os.path.join(logs_dir, f"config_backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt")
        
        # Write the running-config to the file
        with open(file_path, "w") as config_file:
            config_file.write(config_output)

        print(f"Configuration backup has been written to {file_path}")
