import os
import subprocess
import sys
from configuration import *

command = sys.argv[1]

result = subprocess.check_output([command])

if os.path.isfile(mysql_initialization_tmp):
    os.remove(mysql_initialization_tmp)
else:
    with open(mysql_initialization_tmp, "wt") as fout:
        fout.write(result)
