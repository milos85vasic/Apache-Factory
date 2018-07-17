import subprocess
import sys
from Toolkit.commands import *
from Toolkit.system_configuration import arg_prefix

who = sys.argv[1]
what = sys.argv[2]
extra = None

if sys.argv[3]:
    extra = sys.argv[3]

command = "ps -u " + who + " | grep " + what

if extra == arg_prefix + "all":
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
