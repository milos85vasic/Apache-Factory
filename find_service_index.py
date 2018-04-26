import json
import getpass
import sys

from commands import *
from configuration import *
from system_configuration import *

account = getpass.getuser()

system_configuration = get_system_configuration()

service_name = sys.argv[1]
service_home = sys.argv[2]
service = system_configuration[account][service_name]


def get_index(directory):
    for index in service_indexes:
        full_path = directory + "/" + index
        if os.path.isfile(full_path):
            return directory
    return None


service_root_directory = get_index(service_home)
if service_root_directory is not None:
    service[key_services_url] = service_root_directory
    system_configuration[account][service_name] = service
    save_system_configuration(system_configuration)
else:
    for subdirectory in os.walk(service_home):
        service_root_directory = get_index(subdirectory)
        if service_root_directory is not None:
            service[key_services_url] = service_root_directory
            system_configuration[account][service_name] = service
            save_system_configuration(system_configuration)
            break
