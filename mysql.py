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

start = "./mysqld --defaults-extra-file=" + user_home() + "/" + mysql + "/my.conf"

if has_feature(account, feature_mysql):
    steps = [
        concatenate(
            cd(user_home()),
            mkdir(mysql),
            mkdir(mysql + "/" + mysql_installation_dir),
            mkdir(mysql + "/" + mysql_data_dir),
            mkdir(mysql + "/" + mysql_log_dir),
            mkdir(mysql + "/" + mysql_tmp_dir),
            mkdir(mysql + "/" + mysql_sock_dir),
            mkdir(mysql + "/" + mysql_pid_dir),
            mkdir(mysql + "/" + mysql_share_dir),
            wget(mysql_download, destination=(user_home() + "/")),
            clear(),
            extract(user_home() + "/" + mysql_tar_gz, destination=user_home()),
            clear(),
            cd(mysql_tar_gz.replace(".tar.gz", "")),

            # TODO: Git clone and wipe my.conf.matrix

            "cmake ./ -DDOWNLOAD_BOOST=1 -DWITH_BOOST=" + get_home_directory_path(account) + "/Boost",
            "make",
            'make install DESTDIR="' + user_home() + "/" + mysql + "/" + mysql_installation_dir + '"',
            cd(user_home() + "/" + mysql + "/" + mysql_installation_dir + "/usr/local/mysql/bin"),
            initialize,
            start,

            # TODO: the rest of.
            cd(user_home()),
            rm(mysql_tar_gz),
            rm(mysql_tar_gz.replace(".tar.gz", ""))
        )
    ]

    run(steps)
