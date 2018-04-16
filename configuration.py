from os.path import expanduser

default_port = 8080
home = expanduser("~")
apache_home = home + "/Apache2"
apache_conf = apache_home + "/conf"
apache_bin = apache_home + "/bin"
apache_tar_gz = "httpd-2.4.29.tar.gz"
apache_download = "http://www-us.apache.org/dist/httpd/" + apache_tar_gz
apache_extract = home + "/" + apache_tar_gz
apache_extracted = home + "/" + apache_tar_gz.replace(".tar.gz", "")
factory_script = "factory.py"
distribution_script = "distribute.py"
wipe_script = "wipe.py"
apache_factory = "Apache-Factory"
apache_factory_group = "apache_factory"
httpd_conf_matrix = "httpd.conf.matrix"
httpd_conf = "httpd.conf"
httpd_conf_matrix_home_dir_placeholder = "APACHE_FACTORY_HOMEDIR"
httpd_conf_matrix_port_placeholder = "APACHE_FACTORY_PORT"
httpd_conf_matrix_user_placeholder = "APACHE_FACTORY_USER"
httpd_conf_matrix_group_placeholder = "APACHE_FACTORY_GROUP"
httpd_conf_matrix_server_admin_placeholder = "APACHE_FACTORY_SERVER_ADMIN"
apache_factory_configuration_dir = "/usr/share/apache_factory"
content_dir_name = "Content"
default_configuration_json = apache_factory_configuration_dir + "/global_configuration.json"
account_json = "account.json"
configuration_repository = "https://github.com/milos85vasic/Apache-Factory-Config-Default.git"
brotli_repository = "https://github.com/milos85vasic/brotli.git"
brotli_module_repository = "https://github.com/milos85vasic/apache-mod-brotli"
brotli = "Brotli"


def get_home_directory_path(account):
    return "/home/" + account


def content_dir_path(home_path):
    return home_path + "/" + content_dir_name


def content_dir_matrix_path(home_path):
    return home_path + "/" + apache_factory + "/content/index.html"
