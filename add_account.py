import sys
from commands import *
from configuration import *

account = ""

for arg in sys.argv:
    if sys.argv.index(arg) > 0:
        account += arg

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
            cp_dir(apache_factory_full_path, get_apache_factory_directory_path(account)),
            chown(account, get_apache_factory_directory_path(account)),
            chgrp(account, get_apache_factory_directory_path(account)),
            chmod(get_apache_factory_directory_path(account), "750"),
            clear()
        )
    ),
    run_as_user(
        account,
        concatenate(
            mkdir(apache_factory),
            cd(apache_factory),
            git_clone(repository),
            python(factory_script)
        )
    )
]
run(steps)
