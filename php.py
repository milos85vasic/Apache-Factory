import sys
from Toolkit.commands import *
from configuration import *
from Toolkit.system_configuration import *

account = sys.argv[1]


def user_home():
    return get_home_directory_path(account)


system_configuration = get_system_configuration()

configure = "./configure --prefix=" + user_home() + \
            "/" + php + " --with-apxs2=" + user_home() + "/" + apache2 + "/bin/apxs"

if has_feature(account, feature_mysql):
    configure += " --with-mysql=mysqlnd" + \
                 " --enable-fpm --disable-short-tags --with-openssl --with-pcre-regex --with-pcre-jit --with-zlib " + \
                 "--enable-bcmath --with-bz2 --enable-calendar --with-curl --enable-exif --with-gd --enable-intl " + \
                 "--enable-mbstring --with-mysqli=mysqlnd --enable-pcntl --with-pdo-mysql=mysqlnd --enable-soap " + \
                 "--enable-sockets --with-xmlrpc --enable-zip --with-webp-dir --with-jpeg-dir --with-png-dir"

php_archive = php_tar_gz
php_download_url = php_download
php_dir = php_tar_gz.replace(".tar.gz", "")
if has_feature(account, feature_php_5):
    php_archive = php_5636_tar_gz
    php_download_url = php_5636_download
    php_dir = php_5636_tar_gz.replace(".tar.gz", "")

if has_feature(account, feature_mysql):
    mysql_port = default_port_mysql
    if account in system_configuration:
        if key_configuration_port_mysql in system_configuration[account]:
            mysql_port = system_configuration[account][key_configuration_port_mysql]

    steps = [
        concatenate(
            cd(user_home()),
            wget(php_download_url, destination=(user_home() + "/")),
            extract(user_home() + "/" + php_archive, destination=user_home()),
            cd(php_dir),
            configure,
            "make",
            "make install",

            cd(user_home()),
            mkdir(php_conf_php_init_dir),
            git_clone_to(php_conf_repository, "./" + php_conf_php_init_dir),
            cd(user_home() + "/" + apache_factory),
            python(
                "Toolkit/" + wipe_script,
                user_home() + "/" + php_conf_php_init_dir + "/php.ini.matrix",
                user_home() + "/" + php + "/lib/php.ini",
                php_conf_matrix_mysql_socket, user_home() + "/" + mysql + "/" + mysql_sock_dir + "/mysqld.sock",
                php_conf_matrix_mysql_port, str(mysql_port),
                php_conf_matrix_mysql_host, "127.0.0.1",
                php_conf_matrix_mysql_user, "root"
            ),

            cd(user_home()),
            rm(php_archive),
            rm(php_dir)
        )
    ]
    run(steps)
else:
    steps = [
        concatenate(
            cd(user_home()),
            wget(php_download_url, destination=(user_home() + "/")),
            extract(user_home() + "/" + php_archive, destination=user_home()),
            cd(php_archive),
            configure,
            "make",
            "make install",
            cp("php.ini-development", user_home() + "/" + php + "/lib/php.ini"),
            cd(user_home()),
            rm(php_archive),
            rm(php_dir)
        )
    ]
    run(steps)



