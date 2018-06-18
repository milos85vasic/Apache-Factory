import json
import getpass
import sys

from Toolkit.commands import *
from configuration import *
from Toolkit.system_configuration import *

account = getpass.getuser()

system_configuration = get_system_configuration()
vhosts_directory = get_home_directory_path(account) + "/" + apache2 + "/" + apache_vhosts_directory

if account in system_configuration:
    if key_services in system_configuration[account]:
        steps = [
            rm(content_dir_path(get_home_directory_path(account)) + "/" + php_test_script)
        ]

        run(steps)
    else:
        sys.exit()
else:
    sys.exit()

steps = [
    concatenate(
        cd(content_dir_path(get_home_directory_path(account))),
        mkdirs(get_services_directories(account))
    )
]

run(steps)

if account in system_configuration:
    if key_services in system_configuration[account]:
        if key_services in system_configuration[account][key_services]:
            for service in system_configuration[account][key_services][key_services]:
                url = service[key_services_url]
                repository = landing_page_repository_default
                if key_services_repository in service:
                    repository = service[key_services_repository]
                steps = [
                    git_clone_to(repository, content_dir_path(get_home_directory_path(account)) + "/" + url),
                    git_submodule_init(),
                    git_submodule_update(),
                    python(
                        content_dir_path(get_home_directory_path(account)) + "/" + url + "/" + website_setup_script,
                        account,
                        url
                    ),
                    python(
                        find_service_index_script,
                        service[key_services_url],
                        content_dir_path(get_home_directory_path(account)) + "/" + url
                    )
                ]

                run(steps)

system_configuration = get_system_configuration()
if account in system_configuration:
    if key_services in system_configuration[account]:
        if key_services in system_configuration[account][key_services]:
            for service in system_configuration[account][key_services][key_services]:
                url = service[key_services_url]
                urls = None
                if key_services_urls in service:
                    urls = service[key_services_urls]
                root = service[key_service_root]
                logs_home = get_home_directory_path(account) + "/" + apache2 + "/logs"
                destination_file = vhosts_directory + "/" + url + ".conf"
                if not os.path.isfile(destination_file):
                    try:
                        with open(destination_file, 'w') as outfile:
                            port = str(system_configuration[account][key_configuration_port])
                            outfile.write("\n")
                            outfile.write("<VirtualHost *:" + port + ">")
                            outfile.write("\n")
                            outfile.write("\tDocumentRoot " + root)
                            outfile.write("\n")
                            outfile.write("\tServerName " + url)
                            outfile.write("\n")
                            if urls:
                                for alias in urls:
                                    outfile.write("\tServerAlias " + alias)
                                    outfile.write("\n")
                            outfile.write("\tErrorLog " + logs_home + "/" + url + ".error.log")
                            outfile.write("\n")
                            outfile.write("\tLogFormat " + '"%h %l %u %t \\"%r\\" %>s %b"' + " common")
                            outfile.write("\n")
                            outfile.write("\tCustomLog " + logs_home + "/" + url + ".access.log common")
                            outfile.write("\n")
                            outfile.write('\t<Directory "' + root + '">')
                            outfile.write("\n")
                            outfile.write("\t\tAllowOverride All")
                            outfile.write("\n")
                            outfile.write("\t</Directory>")
                            outfile.write("\n")

                            if key_password_protect in system_configuration[account][key_services]:
                                key_pp = key_password_protect
                                for password_protect in system_configuration[account][key_services][key_pp]:
                                    for directory in password_protect[key_password_protect_directories]:
                                        if directory[key_password_protect_service] == url:
                                            outfile.write("\n")
                                            outfile.write(
                                                '\t<Directory "' + root + "/" + directory[
                                                    key_password_protect_path] + '">'
                                            )
                                            outfile.write("\n")
                                            outfile.write("\t\tAuthType Basic")
                                            outfile.write("\n")
                                            outfile.write('\t\tAuthName "Restricted Content"')
                                            outfile.write("\n")
                                            outfile.write(
                                                "\t\tAuthUserFile " + get_home_directory_path(
                                                    account) + "/" + security + "/" +
                                                passwd_file
                                            )
                                            outfile.write("\n")
                                            outfile.write("\t\tRequire valid-user")
                                            outfile.write("\n")
                                            outfile.write("\t</Directory>")
                                            outfile.write("\n\n")

                            outfile.write("</VirtualHost>")
                    except IOError:
                        print("Can't access " + destination_file)

system_configuration = get_system_configuration()
if account in system_configuration:
    if key_services in system_configuration[account]:
        if key_services in system_configuration[account][key_services]:
            for service in system_configuration[account][key_services][key_services]:
                if key_configuration_main_proxy in service:
                    bind_to_account = service[key_configuration_main_proxy]
                    destination_directory = get_home_directory_path(
                        bind_to_account) + "/" + apache2 + "/" + apache_vhosts_directory

                    add_group_permission = "chmod g+rwx " + destination_directory

                    steps = [
                        run_as_su(
                            concatenate(
                                add_to_group(account, bind_to_account),
                                add_group_permission
                            )
                        )
                    ]

                    run(steps)
