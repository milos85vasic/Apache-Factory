import json
import getpass

from Toolkit.commands import *
from configuration import *
from Toolkit.system_configuration import *

start_command = apache_start()
account = getpass.getuser()

system_configuration = get_system_configuration()

configuration_repo = configuration_repository

incrementPortNumber = True

if account in system_configuration:
    if key_services in system_configuration[account]:
        if key_configuration in system_configuration[account][key_services]:
            if key_configuration_repository in system_configuration[account][key_services][key_configuration]:
                configuration_repo = system_configuration[account][key_services][key_configuration][
                    key_configuration_repository
                ]

                if key_explicit_port_number in system_configuration[account][key_services][key_configuration]:
                    if system_configuration[account][key_services][key_configuration][key_explicit_port_number]:
                        incrementPortNumber = False
                        system_configuration[account][key_configuration_port] = system_configuration[account][
                            key_services][key_configuration][key_explicit_port_number]

                        if system_configuration[account][key_configuration_port] < 1024:
                            start_command = run_as_su(apache_start())

if incrementPortNumber:
    system_configuration[key_configuration_port] = system_configuration[key_configuration_port] + 1
    system_configuration[account][key_configuration_port] = system_configuration[key_configuration_port]

save_system_configuration(system_configuration)
php_version = 7
if has_feature(account, feature_php_5):
    php_version = 5

steps = [
    cd("~"),
    rm(apache_conf),
    mkdir(apache_conf),
    chmod(apache_conf, "755"),
    concatenate(
        cd(apache_conf),
        git_clone_to_recursive(configuration_repo, here),
        git_submodule_checkout_each(),
        cd("~")
    ),
    python(
        "Toolkit/" + wipe_script,
        apache_conf + "/" + httpd_conf_matrix,
        apache_conf + "/" + httpd_conf,
        httpd_conf_matrix_home_dir_placeholder, home,
        httpd_conf_matrix_port_placeholder, str(system_configuration[account][key_configuration_port]),
        httpd_conf_matrix_user_placeholder, account,
        httpd_conf_matrix_group_placeholder, account,
        httpd_conf_matrix_server_name_placeholder, account,
        httpd_conf_matrix_server_admin_placeholder, str(system_configuration[account][key_configuration_server_admin]),
        httpd_conf_matrix_php_version, str(php_version)
    ),
    python(services_distribution_script),
    concatenate(
        cd(apache_bin),
        start_command,
        sleep(10),
        cd("~"),
    ),
    curl("http://localhost:" + str(system_configuration[account][key_configuration_port]))
]

run(steps)
