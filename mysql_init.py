import os
import sys
from configuration import *
from mysql_common import *

command = get_mysql_bin_directory() + initialize

steps = [
    command
]

run(command)


# TODO: parse  /home/test1/MySQL/Log/error.log for password.


