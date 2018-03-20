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
        # "sed -i 's/HOMEDIR/new/" + home + "/g'", TODO: USe wipe.py
        cd("~")
    ),
    concatenate(
        cd(apache_bin),
        apache_start(),
        cd("~")
    )
]

run(steps)