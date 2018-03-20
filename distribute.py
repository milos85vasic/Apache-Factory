from commands import *
from configuration import *

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
    concatenate(
        cd(apache_conf),
        python(
            wipe_script,
            httpd_conf_matrix,
            httpd_conf,
            httpd_conf_matrix_home_dir_placeholder,
            home
        ),
        cd("~")
    ),
    concatenate(
        cd(apache_bin),
        apache_start(),
        cd("~")
    )
]

run(steps)
