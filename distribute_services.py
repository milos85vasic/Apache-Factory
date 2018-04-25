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
