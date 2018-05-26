import subprocess
import sys
import re

what = sys.argv[1]
command = "ps -A | grep " + what

ps = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
result = ps.communicate()[0]

# result = "15639 pts/0    00:00:01 mysqld"

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
