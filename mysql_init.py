import os
import random
import sys
from configuration import *
from mysql_common import *
import string

command = get_mysql_bin_directory() + initialize

steps = [
    command
]

run(steps)

alphabet = string.ascii_letters + string.digits
mysql_password = ''.join(random.choice(alphabet) for i in range(20))

print("MySQL root user password: " + mysql_password)
system_configuration[account][key_services][key_credentials] = {feature_mysql: mysql_password}
save_system_configuration(system_configuration)

alter_user = "ALTER USER 'root'@'localhost' IDENTIFIED BY '" + mysql_password + "';"

steps = [
    output(alter_user, mysql_init_tmp),
    get_mysql_bin_directory() + get_start_command_init(user_home()),
    # python(
    #     killer_script,
    #     "mysql"
    # ),

    # TODO: start cmd
    # get_mysql_bin_directory() + get_start_command(user_home())

    # rm_files("*.tmp")
]
run(steps)
