import sys
from commands import *
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


account = sys.argv[1]

system_configuration = get_system_configuration()

initialize = "/mysqld --defaults-file=" + user_home() + "/" + mysql + "/" + mysql_conf_dir + \
             "/my.conf --initialize --user=" + account
