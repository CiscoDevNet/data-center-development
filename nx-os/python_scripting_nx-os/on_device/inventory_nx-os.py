import subprocess

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
    inventory = run_cli_command("show inventory")
    if inventory:
        print("Device Inventory:")
        print(inventory)
        with open("/bootflash/scripts/inventory_log.txt", "a") as log_file:
            log_file.write(f"{inventory}\n")