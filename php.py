import sys
from commands import *
from configuration import *
from system_configuration import *

account = sys.argv[1]


def user_home():
    return get_home_directory_path(account)


system_configuration = get_system_configuration()

configure = "./configure --prefix=" + user_home() + \
            "/" + php + " --with-apxs2=" + user_home() + "/" + apache2 + "/bin/apxs"

if has_feature(account, feature_mysql):
    configure += " --with-mysql=" + user_home() + "/" + mysql

steps = [
    concatenate(
        cd(user_home()),
        wget(php_download, destination=(user_home() + "/")),
        extract(user_home() + "/" + php_tar_gz, destination=user_home()),
        cd(php_tar_gz.replace(".tar.gz", "")),
        configure,
        "make",
        "make install",
        cp("php.ini-development", user_home() + "/" + php + "/lib/php.ini"),
        cd(user_home()),
        rm(php_tar_gz),
        rm(php_tar_gz.replace(".tar.gz", ""))
    )
]

run(steps)
