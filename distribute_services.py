import json
import getpass
import sys

from commands import *
from configuration import *
from system_configuration import *

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

for service in system_configuration[account][key_services][key_services]:
    url = service[key_services_url]
    repository = service[key_services_repository]
    steps = [
        git_clone_to(repository, content_dir_path(get_home_directory_path(account)) + "/" + url),
        python(
            find_service_index_script,
            service[key_services_url],
            content_dir_path(get_home_directory_path(account)) + "/" + url
        )
    ]

    run(steps)

system_configuration = get_system_configuration()
for service in system_configuration[account][key_services][key_services]:
    url = service[key_services_url]
    urls = None
    if key_services_urls in service:
        urls = service[key_services_urls]
    repository = service[key_services_repository]
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
                outfile.write("</VirtualHost>")
        except IOError:
            print("Can't access " + destination_file)
