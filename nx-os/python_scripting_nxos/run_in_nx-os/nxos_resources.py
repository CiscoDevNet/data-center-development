cat << 'EOF' > nxos_resources.py
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

def get_top_processes(processes_output, top_n=5):
    # Assuming 'processes_output' is a newline-delimited string of process information
    processes = processes_output.strip().split('\n')
    # Further parsing may be required depending on the format of 'processes_output'
    top_processes = processes[:top_n]
    return '\n'.join(top_processes)

if __name__ == "__main__":
    print("="*40)
    print("CPU Info:")
    print("="*40)
    cpu_info = run_cli_command("show system resources")
    print(cpu_info)
    print("="*40)
    
    print("Top Processes by Memory Usage:")
    print("="*40)
    memory_info = run_cli_command("show processes memory")
    top_processes = get_top_processes(memory_info, top_n=10)
    print(top_processes)
    print("="*40)
EOF
