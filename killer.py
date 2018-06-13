import subprocess
import sys
from Toolkit.commands import *

who = sys.argv[1]
what = sys.argv[2]

command = "ps -u " + who + " | grep " + what

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
