#!/usr/bin/python

import sys
from Toolkit.commands import *
from Toolkit.system_configuration import *
from configuration import *
from git_info import *

system_configuration = get_system_configuration()

for item in system_configuration.keys():
    account = item
    script = get_home_directory_path(account)
    if not os.path.exists(script):
        exit()

    script += "/" + apache2 + "/bin/apachectl"
    if system_configuration[account][key_configuration_port] < 1024:
        start_command = run_as_su(script + " start")
    else:
        start_command = run_as_user(account, script + " start")

    if os.path.isfile(script):
        steps = [start_command]

        print("We are about to execute:")
        print(script)
        run(steps)
    else:
        print("Cannot execute:")
        print(script)

    if has_feature(account, feature_mysql):
        # MySQL 8.0:
        # script = get_home_directory_path(account) + "/" + mysql + "/" + mysql_installation_dir + \
        #          "/usr/local/mysql/bin/mysqld"

        # My SQL 5.5.60:
        port = default_port_mysql
        if account in system_configuration:
            if key_configuration_port_mysql in system_configuration[account]:
                port = system_configuration[account][key_configuration_port_mysql]
        mysql_full_path = get_home_directory_path(account) + "/" + mysql + "/"
        script = mysql_full_path + mysql_bin_dir + "/mysqld"

        if os.path.isfile(script):
            # MySQL 8.0:
            # script += " --defaults-extra-file=" + get_home_directory_path(account) + "/" + mysql + "/" \
            #           + mysql_conf_dir + "/my.cnf &"

            # My SQL 5.5.60:
            script += " --tmpdir=" + mysql_full_path + "tmp --datadir=" + mysql_full_path + "data " + \
                      "--secure-file-priv=" + mysql_full_path + "priv --port=" + str(port) + " --user=" + account + \
                      " " + "--socket=" + mysql_full_path + "socket/mysqld.sock &"

            steps = [
                run_as_user(account, script)
            ]

            print("We are about to execute:")
            print(script)
            run(steps)
        else:
            print("Cannot execute:")
            print(script)
