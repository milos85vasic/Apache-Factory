import json
import os

from configuration import *
from commands import *

arg_prefix = "--"
arg_server_admin = arg_prefix + "server_admin"
key_configuration_port = "port"
key_configuration_port_mysql = "port_mysql"
key_configuration_server_admin = "server_admin"
key_services = "services"
key_features = "features"
feature_mysql = "mysql"
key_services_url = "url"
key_services_urls = "urls"
key_service_root = "root"
key_credentials = "credentials"
key_services_repository = "repository"
key_password_protect = "password_protect"
key_password_protect_user = "user"
key_password_protect_password = "password"
key_password_protect_directories = "directories"
key_password_protect_service = "service"
key_password_protect_path = "path"
services_file = key_services + ".json"
key_configuration = "configuration"
key_configuration_main_proxy = "main_proxy"
key_explicit_port_number = "explicit_port_number"
key_configuration_repository = "configuration_repository"


def init_system_configuration(arguments):
    if not os.path.isdir(apache_factory_configuration_dir):
        steps = [
            run_as_su(
                concatenate(
                    mkdir(apache_factory_configuration_dir),
                    chmod(apache_factory_configuration_dir, "770")
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
        services_config = json.load(open(services_file))
        account = get_account()
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
        key_configuration_port: default_port,
        key_configuration_port_mysql: default_port_mysql
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


def get_services_directories(account):
    directories = []
    system_configuration = get_system_configuration()
    if account in system_configuration:
        if key_services in system_configuration[account]:
            if key_services in system_configuration[account][key_services]:
                for service in system_configuration[account][key_services][key_services]:
                    directories.append(service[key_services_url])
    return directories


def has_feature(account, feature):
    features = None
    system_configuration = get_system_configuration()

    account_configuration = system_configuration[account]
    if isinstance(account_configuration, dict):
        if key_services in account_configuration:
            if key_features in system_configuration[account][key_services]:
                features = system_configuration[account][key_services][key_features]

    return features and feature in features
