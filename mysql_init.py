import os
import subprocess
import sys
from configuration import *
from mysql_common import *

command = get_mysql_bin_directory() + initialize

result = subprocess.check_output(command.split(" "), shell=True)

print(result)
print("- - - - - - - - - - - -")

if os.path.isfile(mysql_initialization_tmp):
    os.remove(mysql_initialization_tmp)
else:
    with open(mysql_initialization_tmp, "wt") as fout:
        fout.write(result)
