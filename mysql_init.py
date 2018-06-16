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

alter_user = "ALTER USER 'root'@'localhost' IDENTIFIED BY '" + mysql_password + "';"

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
steps = [
    concatenate(
        cd(get_home_directory_path(account) + "/" + mysql),
        mkdir(mysql_tmp_dir),
        mkdir(mysql_priv_dir),
        mkdir(mysql_sock_dir),
        chmod(mysql_priv_dir, "700")
    ),
    # TODO:
    # ./scripts/mysql_install_db --user=test1 --basedir=/home/test1/MySQL/ --datadir=/home/test1/MySQL/data/
    # --port=3307 --tmpdir=/home/test1/MySQL/tmp/ --secure-file-priv=/home/test1/MySQL/priv/

    # TODO: Apsolute paths, add --user=
    # ./mysqld --tmpdir=/home/test1/MySQL/tmp --datadir=/home/test1/MySQL/data --secure-file-priv=/home/test1/MySQL/priv
    #  --port=3307 --user=test1 --socket=/home/test1/MySQL/socket/mysqld.sock
    get_home_directory_path(account) + "/" + mysql + "/" + mysql_bin_dir +
    "/mysqld start --tmpdir=" + mysql_tmp_dir + "/ --datadir="+ mysql_data_dir + "/ " +
    "--secure-file-priv=" + mysql_priv_dir + "/ --port=" + port,
    sleep(10),

    # python(
    #     killer_script,
    #     account,
    #     "mysqld"
    # ),
    # sleep(5),
    # get_home_directory_path(account) + "/" + mysql + "/" + mysql_bin_dir + get_start_command(user_home()),
    #
    # sleep(10),
    # rm_files("*.tmp")
]
run(steps)
