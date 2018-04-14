import json
import getpass

from commands import *
from configuration import *
from system_configuration import *

account = getpass.getuser()

system_configuration = get_system_configuration()
system_configuration[key_configuration_port] = system_configuration[key_configuration_port] + 1
save_system_configuration(system_configuration)

steps = [
    cd("~"),
    clear(),
    rm(apache_conf),
    mkdir(apache_conf),
    chmod(apache_conf, "755"),
    concatenate(
        cd(apache_conf),
        git_clone_into(configuration_repository, here),
        cd("~")
    ),
    clear(),
    python(
        wipe_script,
        apache_conf + "/" + httpd_conf_matrix,
        apache_conf + "/" + httpd_conf,
        httpd_conf_matrix_home_dir_placeholder, home,
        httpd_conf_matrix_port_placeholder, str(system_configuration[key_configuration_port]),
        httpd_conf_matrix_user_placeholder, account,
        httpd_conf_matrix_group_placeholder, account,
        httpd_conf_matrix_server_admin_placeholder, str(system_configuration[account][key_configuration_server_admin])
    ),
    rm(
        apache_conf + "/" + httpd_conf_matrix
    ),
    concatenate(
        cd(apache_bin),
        apache_start(),
        sleep(10),
        cd("~"),
    ),
    clear(),
    curl("http://localhost:" + str(system_configuration["port"]))
]

run(steps)
