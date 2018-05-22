import os
import sys
from configuration import *
from mysql_common import *

command = get_mysql_bin_directory() + initialize

steps = [
    command
]

run(steps)

contains = "A temporary password is generated for root@localhost: "
path = get_mysql_logs_directory() + "/" + "error.log"
with open(path) as fp:
    for cnt, line in enumerate(fp):
        if contains in line:
            split_result = line.split(contains)
            print(split_result[0])
            break
