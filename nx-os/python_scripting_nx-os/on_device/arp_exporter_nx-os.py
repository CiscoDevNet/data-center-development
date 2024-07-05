import subprocess
import csv
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
    arp_output = run_cli_command("show ip arp")
    if arp_output:
        rows = [line.split() for line in arp_output.splitlines()[1:]]  # Skip the header
        with open(f"/bootflash/scripts/arp_table_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv", "w") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Address", "Age", "MAC Address", "Interface"])
            writer.writerows(rows)
