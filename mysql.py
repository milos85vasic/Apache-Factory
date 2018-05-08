import sys
from commands import *
from configuration import *
from system_configuration import *

account = sys.argv[1]


def user_home():
    return get_home_directory_path(account)


system_configuration = get_system_configuration()

# TODO: Obtain my.conf from git repository.
initialize = "./mysqld --defaults-file=" + user_home() + "/" + mysql + "/" + mysql_conf_dir + \
             "/my.conf --initialize-insecure --user=" + account

start = "./mysqld --defaults-extra-file=" + user_home() + "/" + mysql + "/" + mysql_conf_dir + "/my.conf"

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
            mkdir(mysql + "/" + mysql_conf_dir),
            cd(mysql + "/" + mysql_conf_dir),
            git_clone_to(configuration_repository_my_sql, "./"),


            clear(),
            python(
                user_home() + "/" + apache_factory + "/" + wipe_script,
                user_home() + "/" + mysql + "/" + mysql_conf_dir + "/" + mysql_conf_matrix,
                user_home() + "/" + mysql + "/" + mysql_conf_dir + "/" + mysql_conf,

                # TODO: Replace with key value pairs
                httpd_conf_matrix_home_dir_placeholder, home,

            ),


            cd(user_home()),
            wget(mysql_download, destination=(user_home() + "/")),
            clear(),
            extract(user_home() + "/" + mysql_tar_gz, destination=user_home()),
            clear(),
            cd(mysql_tar_gz.replace(".tar.gz", "")),
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
