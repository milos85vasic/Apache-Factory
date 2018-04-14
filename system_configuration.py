import json
import os

from configuration import *

arg_prefix = "--"
key_current_account = "current_account"
arg_server_admin = arg_prefix + "server_admin"
key_configuration_port = "port"
key_configuration_server_admin = "server_admin"


def init_system_configuration(arguments):
    system_configuration = get_system_configuration()
    for arg in arguments:
        if arguments.index(arg) > 0 and not str(arg).startswith(arg_prefix):
            system_configuration[arg] = {key_configuration_server_admin: "root@localhost"}
            system_configuration[key_current_account] = arg
        if str(arg).startswith(arg_server_admin):
            server_admin = str(arg).replace(arg_server_admin + "=", "")
            account = system_configuration[key_current_account]
            system_configuration[account][key_configuration_server_admin] = server_admin
    save_system_configuration(system_configuration)
    return system_configuration


def get_system_configuration():
    system_configuration = {
        key_configuration_port: default_port
    }
    if not os.path.isfile(default_configuration_json):
        try:
            with open(default_configuration_json, 'w') as outfile:
                json.dump(system_configuration, outfile)
        except IOError:
            print("Can't access " + default_configuration_json)
    else:
        system_configuration = json.load(open(default_configuration_json))
    return system_configuration


def save_system_configuration(system_configuration):
    with open(default_configuration_json, 'w') as outfile:
        json.dump(system_configuration, outfile)
