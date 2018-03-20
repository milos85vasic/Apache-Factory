from commands import *
from configuration import *

steps = [
    cd("~"),
    clear(),
    remove(apache_conf),
    mkdir(apache_conf),
    cd(apache_conf),
    # TODO: Clone HTTPD configuration repo.
    cd("~")
]

run(steps)
