import os
import sys
from configuration import *
from mysql_common import *

command = get_mysql_bin_directory() + initialize

steps = [
    command
]

run(command)

contains = "A temporary password is generated for root@localhost: "
path = get_mysql_logs_directory() + "/" + "error.log"
fp = open(path, 'r')

# TODO: parse  /home/test1/MySQL/Log/error.log for password.
