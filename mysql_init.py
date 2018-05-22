import os
import sys
from configuration import *
from mysql_common import *
from subprocess import Popen, PIPE, STDOUT

command = get_mysql_bin_directory() + initialize

p = Popen(command.split(" "), stdin=PIPE, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate()

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print(command)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print(stdout)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print(stderr)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

# TODO: parse  /home/test1/MySQL/Log/error.log for password.

# if os.path.isfile(mysql_initialization_tmp):
#     os.remove(mysql_initialization_tmp)
# else:
#     with open(mysql_initialization_tmp, "wt") as fout:
#         fout.write(result)
