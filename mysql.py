import sys
from commands import *
from configuration import *
from system_configuration import *

account = sys.argv[1]


def user_home():
    return get_home_directory_path(account)


system_configuration = get_system_configuration()

features = None

if key_services in system_configuration[account]:
    if key_features in system_configuration[account][key_services]:
        features = system_configuration[account][key_services][key_features]
else:
    features = [key_feature_mysql]

if features and key_feature_mysql in features:
    steps = [
        concatenate(
            cd(user_home()),
            wget(mysql_download, destination=(user_home() + "/")),
            clear(),
            extract(user_home() + "/" + mysql_tar_gz, destination=user_home()),
            clear(),
            cd(mysql_tar_gz.replace(".tar.gz", "")),
            mkdir("bld"),
            cd("bld"),
            "cmake ../mysql-src",
            "make",
            'make install DESTDIR="' + user_home() + "/" + mysql + '"',
            cd(user_home()),
            rm(mysql_tar_gz),
            rm(mysql_tar_gz.replace(".tar.gz", ""))
        )
    ]

    run(steps)
