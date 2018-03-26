from commands import *
from distribution_utils import *

port = 8080

steps = [
    cd("~"),
    clear(),
    remove(apache_conf),
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
        httpd_conf_matrix_home_dir_placeholder,
        home
    ),
    mv(
        apache_conf + "/" + httpd_conf,
        apache_conf + "/" + httpd_conf_matrix
    ),
    python(
        wipe_script,
        apache_conf + "/" + httpd_conf_matrix,
        apache_conf + "/" + httpd_conf,
        httpd_conf_matrix_port_placeholder,
        str(port)
    ),
    concatenate(
        cd(apache_bin),
        apache_start(),
        sleep(10),
        cd("~"),
    ),
    clear(),
    echo("We are about to ping Apache instance. Please wait."),
    curl("http://localhost:" + str(port))
]

run(steps)
