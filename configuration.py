from os.path import expanduser

default_port = 8080
default_port_mysql = 3306
home = expanduser("~")
php = "Php"
mysql = "MySQL"
mysql_installation_dir = "Release"
mysql_data_dir = "Data"
mysql_log_dir = "Log"
mysql_tmp_dir = "Tmp"
mysql_sock_dir = "Sock"
mysql_pid_dir = "Pid"
mysql_share_dir = "Share"
mysql_conf_dir = "Conf"
apache2 = "Apache2"
apache_home = home + "/" + apache2
php_home = home + "/" + php
mysql_home = home + "/" + mysql
apache_conf = apache_home + "/conf"
apache_bin = apache_home + "/bin"
apache_tar_gz = "httpd-2.4.29.tar.gz"
php_tar_gz = "php-7.2.4.tar.gz"
apache_download = "http://www-us.apache.org/dist/httpd/" + apache_tar_gz
php_download = "http://php.net/distributions/" + php_tar_gz
mysql_tar_gz = "mysql-boost-8.0.11.tar.gz"
mysql_extracted_dir = "mysql-8.0.11"
mysql_download = "https://dev.mysql.com/get/Downloads/MySQL-8.0/" + mysql_tar_gz
apache_extract = home + "/" + apache_tar_gz
apache_extracted = home + "/" + apache_tar_gz.replace(".tar.gz", "")
factory_script = "factory.py"
distribution_script = "distribute.py"
services_distribution_script = "distribute_services.py"
find_service_index_script = "find_service_index.py"
wipe_script = "wipe.py"
apache_factory = "Apache-Factory"
apache_factory_group = "apache_factory"
apache_vhosts_directory = "vhosts"
httpd_conf_matrix = "httpd.conf.matrix"
httpd_conf = "httpd.conf"
mysql_conf_matrix = "my.conf.matrix"
mysql_conf = "my.conf"
httpd_conf_matrix_home_dir_placeholder = "APACHE_FACTORY_HOMEDIR"
httpd_conf_matrix_port_placeholder = "APACHE_FACTORY_PORT"
httpd_conf_matrix_user_placeholder = "APACHE_FACTORY_USER"
httpd_conf_matrix_group_placeholder = "APACHE_FACTORY_GROUP"
httpd_conf_matrix_server_admin_placeholder = "APACHE_FACTORY_SERVER_ADMIN"
my_conf_matrix_port_placeholder = "APACHE_FACTORY_MYSQL_PORT"
my_conf_matrix_sock_dir_placeholder = "APACHE_FACTORY_MYSQL_SOCK_DIR"
my_conf_matrix_pid_dir_placeholder = "APACHE_FACTORY_MYSQL_PID_DIR"
my_conf_matrix_user_placeholder = "APACHE_FACTORY_MYSQL_USER"
my_conf_matrix_base_dir_placeholder = "APACHE_FACTORY_MYSQL_BASE_DIR"
my_conf_matrix_data_dir_placeholder = "APACHE_FACTORY_MYSQL_DATA_DIR"
my_conf_matrix_tmp_dir_placeholder = "APACHE_FACTORY_MYSQL_TMP_DIR"
my_conf_matrix_share_dir_placeholder = "APACHE_FACTORY_MYSQL_SHARE_DIR"
my_conf_matrix_log_dir_placeholder = "APACHE_FACTORY_MYSQL_LOG_DIR"
apache_factory_configuration_dir = "/usr/share/apache_factory"
content_dir_name = "Content"
default_configuration_json = apache_factory_configuration_dir + "/global_configuration.json"
account_json = "account.json"
configuration_repository = "https://github.com/milos85vasic/Apache-Factory-Config-Default.git"
configuration_repository_my_sql = "https://github.com/milos85vasic/Apache-Factory-Config-Default-MySQL.git"
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
service_indexes = ["index.html", "index.htm", "index.php"]
php_test_script = "test.php"
starter_script = "starter.py"
starter_init_script = "starter_init.py"
rc_local = "/etc/rc.d/rc.local"
killer_script = "killer.py"
rpm_fusion_free = "https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm"
rpm_fusion_non_free = "https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-7.noarch.rpm"


def get_home_directory_path(account):
    return "/home/" + account


def content_dir_path(home_path):
    return home_path + "/" + content_dir_name


def content_dir_matrix_path(home_path):
    return home_path + "/" + apache_factory + "/content/index.html"


def content_dir_matrix_path_php(home_path):
    return home_path + "/" + apache_factory + "/content/" + php_test_script
