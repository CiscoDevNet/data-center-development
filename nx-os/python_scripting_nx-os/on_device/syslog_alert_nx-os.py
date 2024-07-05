import subprocess
import re
import smtplib
from email.mime.text import MIMEText

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

def send_email(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "your_email@example.com"
    msg['To'] = "alert_recipient@example.com"

    with smtplib.SMTP("smtp.example.com") as server:
        server.login("your_email@example.com", "your_password")
        server.sendmail("your_email@example.com", ["alert_recipient@example.com"], msg.as_string())

if __name__ == "__main__":
    syslog_output = run_cli_command("show logging last 50")
    if syslog_output:
        for line in syslog_output.splitlines():
            if re.search(r'(error|critical|warning)', line, re.IGNORECASE):
                send_email("NX-OS Alert", line)
