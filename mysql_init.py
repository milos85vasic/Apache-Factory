import string
import random
from configuration import *
from Toolkit.mysql_common import *

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

# MySQL 5.5.60:
mysql_full_path = get_home_directory_path(account) + "/" + mysql + "/"

port = default_port_mysql
if account in system_configuration:
    if key_configuration_port_mysql in system_configuration[account]:
        port = system_configuration[account][key_configuration_port_mysql]

install_db = mysql_full_path + mysql_script_dir + "/mysql_install_db --user=" + account + " --basedir=" + \
             mysql_full_path + " --datadir=" + mysql_full_path + "data/" + " --port=" + str(port) + " --tmpdir=" + \
             mysql_full_path + "tmp/ --secure-file-priv=" + mysql_full_path + "priv/"

install_root = mysql_full_path + mysql_bin_dir + "/mysql --host=127.0.0.1 --user=root --port=" + str(port) + " < " \
               + mysql_init_tmp

steps = [
    output(alter_user, mysql_init_tmp),
    concatenate(
        cd(get_home_directory_path(account) + "/" + mysql),
        mkdir(mysql_tmp_dir),
        mkdir(mysql_priv_dir),
        mkdir(mysql_sock_dir),
        chmod(mysql_priv_dir, "700")
    ),

    install_db,
    python(
        killer_script,
        account,
        "mysqld"
    ),
    sleep(5),
    get_mysql_start_command(account),
    sleep(10),

    install_root,

    python(
        killer_script,
        account,
        "mysqld"
    ),
    sleep(5),
    get_mysql_start_command(account),
    sleep(10),
    rm_files("*.tmp")
]
run(steps)
