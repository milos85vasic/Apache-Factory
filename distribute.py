from commands import *
from configuration import *

steps = [
    cd("~"),
    clear(),
    remove(apache_conf),
    mkdir(apache_conf),
    chmod(apache_conf, "755"),
    cd(apache_conf),
    git_clone(configuration_repository),
    cd("~"),
    cd(apache_bin),
    apache_start(),
    cd("~"),
]

run(steps)
