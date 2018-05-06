import sys
from commands import *
from configuration import *
from system_configuration import *

account = sys.argv[1]


def user_home():
    return get_home_directory_path(account)


system_configuration = get_system_configuration()

# TODO: Obtain my.conf from git repository.
initialize = "./mysqld --defaults-file=" + user_home() + "/" + mysql + "/my.conf --initialize-insecure --user=" \
             + account

if has_feature(account, feature_mysql):
    steps = [
        concatenate(
            cd(user_home()),
            wget(mysql_download, destination=(user_home() + "/")),
            clear(),
            extract(user_home() + "/" + mysql_tar_gz, destination=user_home()),
            clear(),
            cd(mysql_tar_gz.replace(".tar.gz", "")),
            "cmake ./ -DDOWNLOAD_BOOST=1 -DWITH_BOOST=" + get_home_directory_path(account) + "/Boost",
            "make",
            'make install DESTDIR="' + user_home() + "/" + mysql + '"',
            mkdir(user_home() + "/" + mysql_data_dir),
            cd(user_home() + "/" + mysql + "/usr/local/mysql/bin"),
            initialize,
            "./mysqld --defaults-extra-file=" + user_home() + "/" + mysql + "/my.conf",

            # TODO: the rest of.
            cd(user_home()),
            rm(mysql_tar_gz),
            rm(mysql_tar_gz.replace(".tar.gz", ""))
        )
    ]

    run(steps)
