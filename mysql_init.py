import os
import random
import sys
from configuration import *
from Toolkit.mysql_common import *
import string

port = sys.argv[1]

# MySQL 8.0:
# command = get_mysql_bin_directory() + initialize
# steps = [
#     command
# ]
# run(steps)

alphabet = string.ascii_letters + string.digits
mysql_password = ''.join(random.choice(alphabet) for i in range(20))

print("MySQL root user password: " + mysql_password)
system_configuration[account][key_services][key_credentials] = {feature_mysql: mysql_password}
save_system_configuration(system_configuration)

# MySQL 8.0:
# alter_user = "ALTER USER 'root'@'localhost' IDENTIFIED BY '" + mysql_password + "';"

# MySQL 5.5.60:
alter_user = "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('" + mysql_password + "'); " \
             "SET PASSWORD FOR 'root'@'127.0.0.1' = PASSWORD('" + mysql_password + "');"

# MySQL 8.0:
# steps = [
#     output(alter_user, mysql_init_tmp),
#     get_mysql_bin_directory() + get_start_command_init(user_home()),
#     sleep(10),
#     python(
#         killer_script,
#         account,
#         "mysqld"
#     ),
#     sleep(5),
#     get_mysql_bin_directory() + get_start_command(user_home()),
#     sleep(10),
#     rm_files("*.tmp")
# ]
# run(steps)

# MySQL 5.5.560:
mysql_full_path = get_home_directory_path(account) + "/" + mysql + "/"
start_mysql_command = mysql_full_path + mysql_bin_dir + "/mysqld --tmpdir=" + mysql_full_path + "tmp --datadir=" + \
                      mysql_full_path + "data " + "--secure-file-priv=" + mysql_full_path + "priv --port=" + port + \
                      " --user=" + account + " " + "--socket=" + mysql_full_path + "socket/mysqld.sock &"

steps = [
    output(alter_user, mysql_init_tmp),
    concatenate(
        cd(get_home_directory_path(account) + "/" + mysql),
        mkdir(mysql_tmp_dir),
        mkdir(mysql_priv_dir),
        mkdir(mysql_sock_dir),
        chmod(mysql_priv_dir, "700")
    ),

    mysql_full_path + mysql_script_dir +
    "/mysql_install_db --user=" + account + " --basedir=" + mysql_full_path + " --datadir=" + mysql_full_path + "data/"
    + " --port=" + port + " --tmpdir=" + mysql_full_path + "tmp/ --secure-file-priv="+ mysql_full_path + "priv/",

    start_mysql_command,
    sleep(10),

    mysql_full_path + mysql_bin_dir + "/mysql --host=127.0.0.1 --user=root --port=" + str(port) + " < " +
    + mysql_init_tmp,

    python(
        killer_script,
        account,
        "mysqld"
    ),
    sleep(5),
    start_mysql_command,
    sleep(10),
    rm_files("*.tmp")
]
run(steps)
