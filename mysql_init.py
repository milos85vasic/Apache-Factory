import os
import sys
from configuration import *
from mysql_common import *
from subprocess import Popen, PIPE, STDOUT

command = get_mysql_bin_directory() + initialize

p = Popen(command.split(" "), stdin=STDOUT, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate()

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print(stdout)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print(stderr)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

# if os.path.isfile(mysql_initialization_tmp):
#     os.remove(mysql_initialization_tmp)
# else:
#     with open(mysql_initialization_tmp, "wt") as fout:
#         fout.write(result)
