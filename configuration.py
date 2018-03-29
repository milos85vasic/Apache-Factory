from os.path import expanduser

home = expanduser("~")                                                    # Home directory where Apache will be build.
apache_home = home + "/Apache2"                                           # Directory where Apache will be installed.
apache_conf = apache_home + "/conf"                                       # Directory containing Apache configuration.
apache_bin = apache_home + "/bin"                                         # Directory containing Apache binaries.
apache_tar_gz = "httpd-2.4.29.tar.gz"                                     # Name for Apache source to download.
apache_download = "http://www-us.apache.org/dist/httpd/" + apache_tar_gz  # Full url to Apache source code to download.
apache_extract = home + "/" + apache_tar_gz                               # Path to downloaded Apache source.
apache_extracted = home + "/" + apache_tar_gz.replace(".tar.gz", "")      # Path to extract Apache source.
factory_script = "factory.py"                                             # Script performing Apache build.
distribution_script = "distribute.py"                                     # Script performing Apache conf. obtain.
wipe_script = "wipe.py"                                                   # Script performing wiping matrices.
apache_factory = "Apache-Factory"                                         # Directory to clone Apache Factory repo.
apache_factory_group = "apache_factory"                                   # Apache Factory group.
repository = "https://github.com/milos85vasic/Apache-Factory.git"         # Apache Factory repo.
httpd_conf_matrix = "httpd.conf.matrix"                                   # httpd.conf matrix to be used.
httpd_conf = "httpd.conf"                                                 # httpd.conf
httpd_conf_matrix_home_dir_placeholder = "APACHE_FACTORY_HOMEDIR"         # httpd.conf matrix home dir. placeholder.
httpd_conf_matrix_port_placeholder = "APACHE_FACTORY_PORT"                # httpd.conf matrix port placeholder.
apache_factory_configuration_dir = "/usr/share/apache_factory"            # Apache Factory configurations directory.

# JSON file name used tha will be used by tool to store the data.
default_configuration_json = apache_factory_configuration_dir + "/global_configuration.json"

# Repository containing default Apache conf:
configuration_repository = "https://github.com/milos85vasic/Apache-Factory-Config-Default.git"
