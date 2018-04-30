import sys
import pwd
from commands import *
from system_configuration import *
from configuration import *
from git_info import *

set_git_info()
git_configuration = get_git_info()
system_configuration = init_system_configuration(sys.argv)
account = get_account()

try:
    pwd.getpwnam(account)
    print("Account already exists: " + account)
except KeyError:
    steps = [
        run_as_su(
            concatenate(
                cd("~"),
                clear(),
                add_user(account),
                passwd(account),
                add_group(apache_factory_group),
                add_to_group(account, apache_factory_group),
                cd(get_home_directory_path(account)),
                mkdir(apache_factory),
                git_clone(git_configuration[key_repository]),
                cd(apache_factory),
                git_checkout(git_configuration[key_branch]),
                cd(".."),
                chown(account, get_home_directory_path(account)),
                chgrp(account, get_home_directory_path(account)),
                chmod(get_home_directory_path(account), "750"),
                cd("~"),
                cd(apache_factory),
                python(starter_init_script),
                cd("~"),
                clear()
            )
        )
        # ,
        # run_as_user(
        #     account,
        #     concatenate(
        #         python(factory_script)
        #     )
        # )
    ]

    run(steps)
