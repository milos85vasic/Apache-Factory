from commands import *
from distribution_utils import *

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
    concatenate(
        cd(apache_bin),
        apache_start(),
        cd("~")
    ),
    clear(),
    curl("http://localhost:" + get_port())
]

run(steps)
