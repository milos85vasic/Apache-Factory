from os.path import expanduser
from Toolkit.configuration import *

home = expanduser("~")
apache_home = home + "/" + apache2
php_home = home + "/" + php
mysql_home = home + "/" + mysql
apache_conf = apache_home + "/conf"
apache_bin = apache_home + "/bin"
apache_tar_gz = "httpd-2.4.29.tar.gz"
php_tar_gz = "php-7.2.4.tar.gz"
php_5636_tar_gz = "php-5.6.36.tar.gz"
apache_download = "http://archive.apache.org/dist/httpd/" + apache_tar_gz
php_download = "http://php.net/distributions/" + php_tar_gz
php_5636_download = "http://php.net/distributions/" + php_5636_tar_gz

# MySQL 8.0
# mysql_tar_gz = "mysql-boost-8.0.11.tar.gz"
# mysql_extracted_dir = "mysql-8.0.11"
# mysql_download = "https://dev.mysql.com/get/Downloads/MySQL-8.0/" + mysql_tar_gz

# MySQL 5.5.60
# https://dev.mysql.com/get/Downloads/MySQL-5.5/mysql-5.5.60.tar.gz
mysql_extracted_dir = "mysql-5.5.60"
mysql_tar_gz = "mysql-5.5.60.tar.gz"
mysql_download = "https://dev.mysql.com/get/Downloads/MySQL-5.5/" + mysql_tar_gz

apache_extract = home + "/" + apache_tar_gz
apache_extracted = home + "/" + apache_tar_gz.replace(".tar.gz", "")
password_protect_script = "password_protect.py"
grant_privileged_ports_script = "grant_ports.py"
apache_vhosts_directory = "vhosts"
httpd_conf_matrix = "httpd.conf.matrix"
httpd_conf = "httpd.conf"
mysql_conf_matrix = "my.cnf.matrix"
mysql_conf = "my.cnf"
httpd_conf_matrix_home_dir_placeholder = "APACHE_FACTORY_HOMEDIR"
httpd_conf_matrix_port_placeholder = "APACHE_FACTORY_PORT"
httpd_conf_matrix_user_placeholder = "APACHE_FACTORY_USER"
httpd_conf_matrix_group_placeholder = "APACHE_FACTORY_GROUP"
httpd_conf_matrix_server_name_placeholder = "APACHE_FACTORY_SERVER_NAME"
httpd_conf_matrix_server_admin_placeholder = "APACHE_FACTORY_SERVER_ADMIN"
httpd_conf_matrix_php_version = "APACHE_FACTORY_PHP_VERSION"
my_conf_matrix_port_placeholder = "APACHE_FACTORY_MYSQL_PORT"
my_conf_matrix_sock_dir_placeholder = "APACHE_FACTORY_MYSQL_SOCK_DIR"
my_conf_matrix_pid_dir_placeholder = "APACHE_FACTORY_MYSQL_PID_DIR"
my_conf_matrix_user_placeholder = "APACHE_FACTORY_MYSQL_USER"
my_conf_matrix_base_dir_placeholder = "APACHE_FACTORY_MYSQL_BASE_DIR"
my_conf_matrix_data_dir_placeholder = "APACHE_FACTORY_MYSQL_DATA_DIR"
my_conf_matrix_tmp_dir_placeholder = "APACHE_FACTORY_MYSQL_TMP_DIR"
my_conf_matrix_share_dir_placeholder = "APACHE_FACTORY_MYSQL_SHARE_DIR"
my_conf_matrix_log_dir_placeholder = "APACHE_FACTORY_MYSQL_LOG_DIR"
php_conf_repository = "https://github.com/milos85vasic/Apache-Factory-Config-Default-PHP.git"
php_conf_matrix_mysql_socket = "APACHE_FACTORY_MYSQL_SOCKET"
php_conf_matrix_mysql_port = "APACHE_FACTORY_MYSQL_PORT"
php_conf_matrix_mysql_host = "APACHE_FACTORY_MYSQL_HOST"
php_conf_matrix_mysql_user = "APACHE_FACTORY_MYSQL_USER"
php_conf_php_init_dir = "Php.Init.Configuration"
landing_page_repository_default = "https://github.com/milos85vasic/Apache-Factory-Landing-Default.git"
configuration_repository = "https://github.com/milos85vasic/Apache-Factory-Config-Default.git"
# MySQL 8.0
# configuration_repository_my_sql = "https://github.com/milos85vasic/Apache-Factory-Config-Default-MySQL-8.0.git"
# MySQL 5.5.60:
configuration_repository_my_sql = "https://github.com/milos85vasic/Apache-Factory-Config-Default-MySQL-5.5.60.git"
brotli_installation_script = "brotli.py"
brotli_repository = "https://github.com/milos85vasic/brotli.git"
brotli_module_repository = "https://github.com/milos85vasic/apache-mod-brotli"
brotli = "Brotli"
brotli_module = "Brotli_Module"
php_installation_script = "php.py"
php_src = "php-src-php-7.0.29"
mysql_installation_script = "mysql.py"
mysql_initialization_script = "mysql_init.py"
mysql_initialization_tmp = "mysql_init.tmp"
php_test_script = "test.php"
starter_script = "starter.py"
starter_init_script = "starter_init.py"
killer_script = "killer.py"
main_proxy_script = "main_proxy.py"
security = "Security"
passwd_file = ".htpasswd"
website_setup_dir = "Setup"
website_setup_script = "setup_website.py"


def content_dir_matrix_path(home_path):
    return home_path + "/" + apache_factory + "/content/index.html"


def content_dir_matrix_path_php(home_path):
    return home_path + "/" + apache_factory + "/content/" + php_test_script
