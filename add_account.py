import sys
import pwd
from Toolkit.commands import *
from Toolkit.system_configuration import *
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
                add_user(account),
                passwd(account),
                add_group(apache_factory_group),
                add_to_group(account, apache_factory_group),
                chgrp(apache_factory_group, apache_factory_configuration_dir),
                cd(get_home_directory_path(account)),
                mkdir(apache_factory),
                git_clone(git_configuration[key_repository]),
                cd(apache_factory),
                git_checkout(git_configuration[key_branch]),
                git_submodule_init(),
                git_submodule_update(),
                cd(".."),
                chown(account, get_home_directory_path(account)),
                chgrp(account, get_home_directory_path(account)),
                chmod(get_home_directory_path(account), "750"),
                cd("~"),
                cd(apache_factory),
                python(starter_init_script),
                cd("~")
            )
        ),
        run_as_user(
            account,
            concatenate(
                python(factory_script)
            )
        ),
        run_as_user(
            account,
            python(main_proxy_script)
        )
    ]

    run(steps)
