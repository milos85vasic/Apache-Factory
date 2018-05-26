import subprocess
import sys
from commands import *

what = sys.argv[1]
command = "ps -A | grep " + what

ps = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
result = ps.communicate()[0]

lines = str(result).split("\n")

for line in lines:
    if line.endswith(what):
        pid = ""
        for char in line.strip():
            if str(char).isdigit():
                pid += char
            else:
                break
        print(line)
        print("We are about to kill: " + str(pid))
        steps = [
            kill(str(pid))
        ]

        run(steps)
