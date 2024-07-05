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
    # Ensure the directory exists
    log_dir = "/bootflash/scripts/inventory-logs"
    os.makedirs(log_dir, exist_ok=True)

    inventory = run_cli_command("show inventory")
    if inventory:
        log_file_path = os.path.join(log_dir, "inventory_log.txt")
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            log_file.write(f"{inventory}\n")
            log_file.write("="*80 + "\n")
