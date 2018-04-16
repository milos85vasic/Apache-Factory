import sys
from commands import *
from configuration import *
from system_configuration import *

account = sys.argv[1]


def user_home():
    return get_home_directory_path(account)


steps = [
    concatenate(
        cd(get_home_directory_path(account)),
        wget(php_download, destination=(user_home() + "/")),
        clear(),
        extract(user_home() + "/" + php_tar_gz, destination=user_home()),
        clear(),
        cd(php_src)
    )
]

run(steps)
