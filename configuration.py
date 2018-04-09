from os.path import expanduser

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
apache_factory_full_path = home + "/" + apache_factory
apache_factory_group = "apache_factory"
repository = "https://github.com/milos85vasic/Apache-Factory.git"
httpd_conf_matrix = "httpd.conf.matrix"
httpd_conf = "httpd.conf"
httpd_conf_matrix_home_dir_placeholder = "APACHE_FACTORY_HOMEDIR"
httpd_conf_matrix_port_placeholder = "APACHE_FACTORY_PORT"
apache_factory_configuration_dir = "/usr/share/apache_factory"
content_dir_name = "Content"
content_dir_matrix_path = apache_factory_full_path + "/" + content_dir_name + "/assets/index.html"
content_dir_path = home + "/" + content_dir_name
default_configuration_json = apache_factory_configuration_dir + "/global_configuration.json"
configuration_repository = "https://github.com/milos85vasic/Apache-Factory-Config-Default.git"


def get_apache_factory_directory_path(account):
    return "/home/" + account + "/" + apache_factory


def get_home_directory_path(account):
    return "/home/" + account
