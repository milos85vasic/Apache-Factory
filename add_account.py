import sys
from Toolkit.system_configuration import *
from configuration import *
from Toolkit.git_info import *
from pwd import *

steps = [
    run_as_su(
        add_group(apache_factory_group)
    )
]

run(steps)

set_git_info()
git_configuration = get_git_info()
system_configuration = init_system_configuration(sys.argv)
account = get_account()


def get_main_proxy(account_to_check):
    if account_to_check in system_configuration:
        if key_services in system_configuration[account_to_check]:
            if key_services in system_configuration[account_to_check][key_services]:
                for service in system_configuration[account_to_check][key_services][key_services]:
                    if key_configuration_main_proxy in service:
                        main_proxy = service[key_configuration_main_proxy]
                        print("Main proxy: " + main_proxy)
                        return main_proxy
    print("No main proxy found for the account: " + account_to_check)
    return account_to_check


try:
    getpwnam(account)
    print("Account already exists: " + account)
except KeyError:
    steps = [
        run_as_su(
            concatenate(
                cd("~"),
                add_user(account),
                passwd(account),
                add_to_group(account, apache_factory_group),
                chgrp(apache_factory_group, apache_factory_configuration_dir),
                cd(get_home_directory_path(account)),
                mkdir(apache_factory),
                cd(apache_factory),
                git_clone_to_recursive(git_configuration[key_repository], here),
                git_checkout(git_configuration[key_branch]),
                git_submodule_checkout_each(),
                cd(".."),  # TODO: Refactor into 'back' variable.
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
            get_main_proxy(account),
            python("Toolkit/" + main_proxy_script, account)
        )
    ]

    run(steps)
