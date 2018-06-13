import os
import random
import sys
from configuration import *
from Toolkit.mysql_common import *
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
    sleep(10),
    python(
        killer_script,
        account,
        "mysqld"
    ),
    sleep(5),
    get_mysql_bin_directory() + get_start_command(user_home()),
    sleep(10),
    rm_files("*.tmp")
]
run(steps)
