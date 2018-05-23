#!/usr/bin/python

import sys
from commands import *
from system_configuration import *
from configuration import *
from git_info import *

system_configuration = get_system_configuration()

for item in system_configuration.keys():
    account = item
    script = get_home_directory_path(account)
    if not os.path.exists(script):
        exit()

    script += "/" + apache2 + "/bin/apachectl"
    if os.path.isfile(script):
        steps = [
            run_as_user(
                account,
                script + " start"
            )
        ]

        print("We are about to execute:")
        print(script)
        run(steps)
    else:
        print("Cannot execute:")
        print(script)

    if has_feature(account, feature_mysql):
        script = get_home_directory_path(account) + "/" + mysql + "/" + mysql_installation_dir + \
                 "/usr/local/mysql/bin/mysqld"

        if os.path.isfile(script):
            script += " --defaults-extra-file=" + get_home_directory_path(account) + "/" + mysql + "/" \
                      + mysql_conf_dir + "/my.conf &"

            steps = [
                run_as_user(account, script)
            ]

            print("We are about to execute:")
            print(script)
            run(steps)
        else:
            print("Cannot execute:")
            print(script)
