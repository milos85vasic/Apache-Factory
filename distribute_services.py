import json
import getpass

from commands import *
from configuration import *
from system_configuration import *

account = getpass.getuser()

system_configuration = get_system_configuration()
vhosts_directory = get_home_directory_path(account) + "/" + apache2 + "/" + apache_vhosts_directory

steps = [
    concatenate(
        cd(content_dir_path(get_home_directory_path(account))),
        mkdirs(get_services_directories(account))
    )
]

run(steps)

for service in system_configuration[account][key_services]:
    url = service[key_services_url]
    repository = service[key_services_repository]
    steps = [
        git_clone_to(repository, content_dir_path(get_home_directory_path(account)) + "/" + url),
        python(
            find_service_index_script,
            service[key_services_url],
            content_dir_path(get_home_directory_path(account)) + "/" + url
        ),
        mkdir(vhosts_directory)
    ]

    run(steps)

system_configuration = get_system_configuration()
for service in system_configuration[account][key_services]:
    url = service[key_services_url]
    repository = service[key_services_repository]
    root = service[key_service_root]
    destination_file = vhosts_directory + "/" + url + ".conf"
    if not os.path.isfile(destination_file):
        try:
            with open(destination_file, 'w') as outfile:
                outfile.write("NameVirtualHost " + url)
        except IOError:
            print("Can't access " + destination_file)
