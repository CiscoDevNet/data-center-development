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

if __name__ == "__main__":
    config_output = run_cli_command("show running-config")
    if config_output:
        with open(f"/bootflash/scripts/config_backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt", "w") as config_file:
            config_file.write(config_output)
