import json
import getpass

from commands import *
from configuration import *
from system_configuration import *

account = getpass.getuser()

system_configuration = get_system_configuration()

configuration_repo = configuration_repository

incrementPortNumber = True

print(system_configuration)

if key_configuration in system_configuration:
    if key_configuration_repository in system_configuration[key_configuration]:
            configuration_repo = system_configuration[key_configuration][key_configuration_repository]
            if key_explicit_port_number in system_configuration[key_configuration]:
                if system_configuration[key_configuration][key_explicit_port_number]:
                    incrementPortNumber = False

# if incrementPortNumber:
#     system_configuration[key_configuration_port] = system_configuration[key_configuration_port] + 1
#     system_configuration[account][key_configuration_port] = system_configuration[key_configuration_port]
#
# save_system_configuration(system_configuration)
#
print("Configuration repository: " + configuration_repo)
#
# steps = [
#     cd("~"),
#     clear(),
#     rm(apache_conf),
#     mkdir(apache_conf),
#     chmod(apache_conf, "755"),
#     concatenate(
#         cd(apache_conf),
#         git_clone_to(configuration_repo, here),
#         cd("~")
#     ),
#     clear(),
#     python(
#         wipe_script,
#         apache_conf + "/" + httpd_conf_matrix,
#         apache_conf + "/" + httpd_conf,
#         httpd_conf_matrix_home_dir_placeholder, home,
#         httpd_conf_matrix_port_placeholder, str(system_configuration[key_configuration_port]),
#         httpd_conf_matrix_user_placeholder, account,
#         httpd_conf_matrix_group_placeholder, account,
#         httpd_conf_matrix_server_name_placeholder, account,
#         httpd_conf_matrix_server_admin_placeholder, str(system_configuration[account][key_configuration_server_admin])
#     ),
#     python(services_distribution_script),
#     concatenate(
#         cd(apache_bin),
#         apache_start(),
#         sleep(10),
#         cd("~"),
#     ),
#     clear(),
#     curl("http://localhost:" + str(system_configuration["port"]))
# ]
#
# run(steps)
