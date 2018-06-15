import sys
from Toolkit.commands import *
from configuration import *
from Toolkit.system_configuration import *
from Toolkit.mysql_common import *

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
            # MySQL 5.5.60:
            mkdir(mysql + "/" + mysql_bin_dir),
            mkdir(mysql + "/" + mysql_lib_dir),
            mkdir(mysql + "/" + mysql_plugin_dir),
            mkdir(mysql + "/" + mysql_priv_dir),
            mkdir(mysql + "/" + mysql_bench_dir),
            mkdir(mysql + "/" + mysql_script_dir),
            # MySQL 5.5.60 - end.
            mkdir(mysql + "/" + mysql_log_dir),
            mkdir(mysql + "/" + mysql_tmp_dir),
            mkdir(mysql + "/" + mysql_sock_dir),
            mkdir(mysql + "/" + mysql_pid_dir),
            mkdir(mysql + "/" + mysql_share_dir),
            mkdir(mysql + "/" + mysql_conf_dir),
            cd(mysql + "/" + mysql_conf_dir),
            git_clone_to(configuration_repository_my_sql, "./"),
            git_submodule_init(),
            git_submodule_update(),
            python(
                user_home() + "/" + apache_factory + "/Toolkit/" + wipe_script,
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

            # MySQL 8.0:
            # "cmake ./ -DDOWNLOAD_BOOST=1 -DWITH_BOOST=" + get_home_directory_path(account) + "/Boost",

            # MySQL 5.5.60:
            "cmake ./ -DCMAKE_INSTALL_PREFIX="
            + get_home_directory_path(account) + "/" + mysql + "/"
            " -DINSTALL_BINDIR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_bin_dir +
            " -DINSTALL_LIBDIR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_lib_dir +
            " -DINSTALL_MYSQLSHAREDIR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_share_dir +
            " -DINSTALL_SHAREDIR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_share_dir +
            " -DINSTALL_PLUGINDIR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_plugin_dir +
            " -DINSTALL_SBINDIR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_installation_dir +
            " -DINSTALL_SCRIPTDIR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_script_dir +
            " -DINSTALL_SECURE_FILE_PRIVDIR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_priv_dir +
            " -DINSTALL_SQLBENCHDIR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_bench_dir +
            " -DMYSQL_DATADIR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_data_dir +
            " -DODBC_INCLUDES="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_lib_dir +
            " -DODBC_LIB_DIR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_lib_dir +
            " -DSYSCONFDIR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_conf_dir +
            " -DTMPDIR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_tmp_dir +
            " -DMYSQL_UNIX_ADDR="
            + get_home_directory_path(account) + "/" + mysql + "/" + mysql_sock_dir + "/mysql.sock"
            " -DMYSQL_TCP_PORT="
            + str(system_configuration[key_configuration_port_mysql])

            ,
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
