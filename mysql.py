import sys
from commands import *
from configuration import *
from system_configuration import *
from mysql_common import *


def get_start_command(account_home):
    return "/mysqld --defaults-extra-file=" + account_home + "/" + mysql + "/" + mysql_conf_dir + "/my.conf &"


system_configuration = get_system_configuration()

start = "." + get_start_command(user_home())



if has_feature(account, feature_mysql):
    steps = [
        concatenate(
            cd(user_home()),
            # mkdir(mysql),
            # mkdir(mysql + "/" + mysql_installation_dir),
            # mkdir(mysql + "/" + mysql_data_dir),
            # mkdir(mysql + "/" + mysql_log_dir),
            # mkdir(mysql + "/" + mysql_tmp_dir),
            # mkdir(mysql + "/" + mysql_sock_dir),
            # mkdir(mysql + "/" + mysql_pid_dir),
            # mkdir(mysql + "/" + mysql_share_dir),
            # mkdir(mysql + "/" + mysql_conf_dir),
            # cd(mysql + "/" + mysql_conf_dir),
            # git_clone_to(configuration_repository_my_sql, "./"),
            # clear(),
            # python(
            #     user_home() + "/" + apache_factory + "/" + wipe_script,
            #     user_home() + "/" + mysql + "/" + mysql_conf_dir + "/" + mysql_conf_matrix,
            #     user_home() + "/" + mysql + "/" + mysql_conf_dir + "/" + mysql_conf,
            #     my_conf_matrix_port_placeholder, str(system_configuration[key_configuration_port_mysql]),
            #     my_conf_matrix_user_placeholder, account,
            #     my_conf_matrix_sock_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_sock_dir,
            #     my_conf_matrix_pid_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_pid_dir,
            #     my_conf_matrix_base_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_installation_dir,
            #     my_conf_matrix_data_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_data_dir,
            #     my_conf_matrix_tmp_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_tmp_dir,
            #     my_conf_matrix_share_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_share_dir,
            #     my_conf_matrix_log_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_log_dir
            # ),
            # clear(),
            # cd(user_home()),
            # wget(mysql_download, destination=(user_home() + "/")),
            # clear(),
            # extract(user_home() + "/" + mysql_tar_gz, destination=user_home()),
            # clear(),
            cd(mysql_extracted_dir),
            # "cmake ./ -DDOWNLOAD_BOOST=1 -DWITH_BOOST=" + get_home_directory_path(account) + "/Boost",
            # "make",
            'make install DESTDIR="' + user_home() + "/" + mysql + "/" + mysql_installation_dir + '"',
        ),
        cd(user_home() + "/" + apache_factory),
        python(
            mysql_initialization_script,
            account
        ),
        # cd(get_mysql_bin_directory()),
        # start,

        # TODO: the rest of.
        cd(user_home()),
        rm(mysql_tar_gz),
        rm(mysql_tar_gz.replace(".tar.gz", ""))
    ]
    run(steps)
