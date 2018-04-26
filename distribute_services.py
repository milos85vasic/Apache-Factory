import json
import getpass

from commands import *
from configuration import *
from system_configuration import *

account = getpass.getuser()

system_configuration = get_system_configuration()

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
        python(find_service_index_script, service, content_dir_path(get_home_directory_path(account)) + "/" + str(url))
    ]

    run(steps)
