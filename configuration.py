from os.path import expanduser

home = expanduser("~")                                                    # Home directory where Apache will be build.
apache_home = home + "/Apache2"                                           # Directory where Apache will be installed.
apache_conf = apache_home + "/conf"                                       # Directory containing Apache configuration.
apache_tar_gz = "httpd-2.4.29.tar.gz"                                     # Name for Apache source to download.
apache_download = "http://www-us.apache.org/dist/httpd/" + apache_tar_gz  # Full url to Apache source code to download.
apache_extract = apache_home + "/" + apache_tar_gz                        # Path to downloaded Apache source.
apache_extracted = home + "/" + apache_tar_gz.replace(".tar.gz", "")      # Path to extract Apache source.
factory_script = "factory.py"                                             # Script performing Apache build.
distribution_script = "distribute.py"                                     # Script performing Apache conf. obtain.
apache_factory = "Apache-Factory"                                         # Directory to clone Apache Factory repo.
repository = "https://github.com/milos85vasic/Apache-Factory.git"         # Apache Factory repo.
configuration_repository = ""                                             # Repository containing default Apache conf.
