import sys
from commands import *
from system_configuration import *
from configuration import *
from git_info import *

account = ""

for arg in sys.argv:
    if sys.argv.index(arg) > 0 and not str(sys.argv).startswith(arg_prefix):
        account = arg

set_git_info()
init_system_configuration(sys.argv)
git_configuration = get_git_info()

steps = [
    run_as_su(
        concatenate(
            cd("~"),
            clear(),
            add_user(account),
            passwd(account),
            add_group(apache_factory_group),
            add_to_group(account, apache_factory_group),
            mkdir(apache_factory_configuration_dir),
            chmod(apache_factory_configuration_dir, "770"),
            chgrp(apache_factory_group, apache_factory_configuration_dir),
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
            clear()
        )
    ),
    run_as_user(
        account,
        concatenate(
            python(factory_script)
        )
    )
]

run(steps)
