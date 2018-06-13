import sys
from Toolkit.commands import *
from configuration import *
from system_configuration import *


def user_home():
    return get_home_directory_path(account)


def get_mysql_bin_directory():
    return user_home() + "/" + mysql + "/" + mysql_installation_dir + "/usr/local/mysql/bin"


def get_mysql_logs_directory():
    return user_home() + "/" + mysql + "/" + mysql_log_dir


def get_start_command(account_home):
    return "/mysqld --defaults-extra-file=" + account_home + "/" + mysql + "/" + mysql_conf_dir + "/my.conf &"


def get_start_command_init(account_home):
    return "/mysqld --defaults-extra-file=" + account_home + "/" + mysql + "/" + mysql_conf_dir \
           + "/my.conf --init-file=" + account_home + "/" + apache_factory + "/" + mysql_init_tmp + " &"


account = sys.argv[1]
mysql_init_tmp = "init.tmp"

system_configuration = get_system_configuration()

initialize = "/mysqld --defaults-file=" + user_home() + "/" + mysql + "/" + mysql_conf_dir + \
             "/my.conf --initialize --user=" + account
