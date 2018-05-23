#!/usr/bin/python

import sys
from commands import *
from system_configuration import *
from configuration import *
from git_info import *
from mysql import get_start_command

system_configuration = get_system_configuration()

for item in system_configuration.keys():
    account = item
    script = get_home_directory_path(account)
    script += "/" + apache2 + "/bin/apachectl"
    if os.path.isfile(script):
        steps = [
            run_as_user(
                account,
                script + " start"
            )
        ]

        run(steps)

    if has_feature(account, feature_mysql):
        script = get_home_directory_path(account) + "/" + mysql + "/" + mysql_installation_dir + "/usr/local/mysql/bin"
        script += get_start_command(get_home_directory_path(account))
        if os.path.isfile(script):
            steps = [
                run_as_user(account, script)
            ]

            run(steps)
