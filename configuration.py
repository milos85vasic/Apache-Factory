from os.path import expanduser

home = expanduser("~")

apache_home = home + "/Apache2"
apache_conf = apache_home + "/conf"
apache_tar_gz = "httpd-2.4.29.tar.gz"
apache_download = "http://www-us.apache.org/dist//httpd/" + apache_tar_gz
apache_extract = apache_home + "/" + apache_tar_gz
apache_extracted = home + "/" + apache_tar_gz.replace(".tar.gz", "")
factory_script = "factory.py"
distribution_script = "distribute.py"
apache_factory = "Apache-Factory"
repository = "https://github.com/milos85vasic/Apache-Factory.git"
