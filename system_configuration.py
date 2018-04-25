import json
import os

from configuration import *
from commands import *

arg_prefix = "--"
arg_server_admin = arg_prefix + "server_admin"
key_configuration_port = "port"
key_configuration_server_admin = "server_admin"
key_services = "services"
services_file = key_services + ".json"


def init_system_configuration(arguments):
    steps = [
        run_as_su(
            concatenate(
                mkdir(apache_factory_configuration_dir),
                chmod(apache_factory_configuration_dir, "770"),
                chgrp(apache_factory_group, apache_factory_configuration_dir),
            )
        )
    ]

    run(steps)

    system_configuration = get_system_configuration()
    for arg in arguments:
        if arguments.index(arg) > 0 and not str(arg).startswith(arg_prefix):
            system_configuration[arg] = {key_configuration_server_admin: "root@localhost"}
            account = arg
            save_account(account)
        if str(arg).startswith(arg_server_admin):
            if arguments.index(arg) == 1:
                print("First argument must be name of the account!")
                exit(1)
            server_admin = str(arg).replace(arg_server_admin + "=", "")
            account = get_account()
            system_configuration[account][key_configuration_server_admin] = server_admin
            if os.path.isfile(services_file):
                services_config = json.load(services_file)
                system_configuration[account][key_services] = services_config
    save_system_configuration(system_configuration)

    steps = [
        run_as_su(
            concatenate(
                chmod(default_configuration_json, "770"),
                chgrp(apache_factory_group, default_configuration_json),
            )
        )
    ]

    run(steps)

    return system_configuration


def get_account():
    return json.load(open(account_json))


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


def save_account(account):
    with open(account_json, 'w') as outfile:
        json.dump(account, outfile)


def save_system_configuration(system_configuration):
    with open(default_configuration_json, 'w') as outfile:
        json.dump(system_configuration, outfile)
