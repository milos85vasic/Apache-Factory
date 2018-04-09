import json

from commands import *
from configuration import *

system_configuration = {
    "port": 8080
}

if not os.path.isfile(default_configuration_json):
    try:
        with open(default_configuration_json, 'w') as outfile:
            json.dump(system_configuration, outfile)
    except IOError:
        print("Can't access " + default_configuration_json)
else:
    system_configuration = json.load(open(default_configuration_json))
    system_configuration["port"] = system_configuration["port"] + 1
    with open(default_configuration_json, 'w') as outfile:
        json.dump(system_configuration, outfile)

steps = [
    cd("~"),
    clear(),
    rm(apache_conf),
    mkdir(apache_conf),
    chmod(apache_conf, "755"),
    concatenate(
        cd(apache_conf),
        git_clone_into(configuration_repository, here),
        cd("~")
    ),
    clear(),
    python(
        wipe_script,
        apache_conf + "/" + httpd_conf_matrix,
        apache_conf + "/" + httpd_conf,
        httpd_conf_matrix_home_dir_placeholder, home,
        httpd_conf_matrix_port_placeholder, str(system_configuration["port"])
    ),
    rm(
        apache_conf + "/" + httpd_conf_matrix
    ),
    concatenate(
        cd("~"),
        cp(content_dir_matrix_path, "./" + content_dir_name)
    ),
    concatenate(
        cd(apache_bin),
        apache_start(),
        sleep(10),
        cd("~"),
    ),
    clear(),
    curl("http://localhost:" + str(system_configuration["port"]))
]

run(steps)
