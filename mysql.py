import sys
from commands import *
from configuration import *
from system_configuration import *
from mysql_common import *

if has_feature(account, feature_mysql):
    if has_feature(account, feature_mysql):
        system_configuration[key_configuration_port_mysql] = system_configuration[key_configuration_port_mysql] + 1
        system_configuration[account][key_configuration_port_mysql] = system_configuration[key_configuration_port_mysql]

    save_system_configuration(system_configuration)
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
            python(
                user_home() + "/" + apache_factory + "/" + wipe_script,
                user_home() + "/" + mysql + "/" + mysql_conf_dir + "/" + mysql_conf_matrix,
                user_home() + "/" + mysql + "/" + mysql_conf_dir + "/" + mysql_conf,
                my_conf_matrix_port_placeholder, str(system_configuration[key_configuration_port_mysql]),
                my_conf_matrix_user_placeholder, account,
                my_conf_matrix_sock_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_sock_dir,
                my_conf_matrix_pid_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_pid_dir,
                my_conf_matrix_base_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_installation_dir,
                my_conf_matrix_data_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_data_dir,
                my_conf_matrix_tmp_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_tmp_dir,
                my_conf_matrix_share_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_share_dir,
                my_conf_matrix_log_dir_placeholder, user_home() + "/" + mysql + "/" + mysql_log_dir
            ),
            cd(user_home()),
            wget(mysql_download, destination=(user_home() + "/")),
            extract(user_home() + "/" + mysql_tar_gz, destination=user_home()),
            cd(mysql_extracted_dir),
            "cmake ./ -DDOWNLOAD_BOOST=1 -DWITH_BOOST=" + get_home_directory_path(account) + "/Boost",
            "make",
            'make install DESTDIR="' + user_home() + "/" + mysql + "/" + mysql_installation_dir + '"',
        ),
        cd(user_home() + "/" + apache_factory),
        python(
            mysql_initialization_script,
            account
        ),
        concatenate(
            cd(user_home()),
            rm(mysql_tar_gz),
            rm(mysql_tar_gz.replace(".tar.gz", "")),
            rm(mysql_tar_gz.replace(".tar.gz", "").replace("boost-", ""))
        )
    ]
    run(steps)
