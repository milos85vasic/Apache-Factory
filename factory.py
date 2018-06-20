import getpass
from Toolkit.commands import *
from configuration import *

account = getpass.getuser()


def user_home():
    return get_home_directory_path(account)


steps = [
    run_as_su(
        concatenate(
            "yum localinstall -y --nogpgcheck " + rpm_fusion_free + " " + rpm_fusion_non_free,
            get_yum_group("Development Tools"),
            get_yum(
                "epel-release",
                "openssl-devel",
                "gcc",
                "make",
                "cmake",
                "automake",
                "libtool",
                "apr-devel",
                "apr-util-devel",
                "wget",
                "git",
                "sqlite",
                "libxml2",
                "libxml2-devel",
                "ncurses-devel",
                "python-pip",
                "lynx",
                "links",
                "autoconf",
                "re2c",
                "bison",
                "bzip2-devel",
                "libcurl-devel",
                "libpng-devel",
                "libicu-devel",
                "gcc-c++",
                "libmcrypt-devel",
                "libwebp-devel",
                "libjpeg-devel",
                "httpd-devel"
            ),
            pip_upgrade(),
            add_to_group(account, apache_factory_group),
            mkdir(content_dir_path(user_home())),
            chown(account, content_dir_path(user_home())),
            chgrp(account, content_dir_path(user_home())),
            run_as_user(
                account,
                concatenate(
                    cd("~"),
                    mkdir(apache_home),
                    mkdir(apache_home + "/" + apache_vhosts_directory),
                    mkdir(php_home),
                    mkdir(mysql_home),
                    cp(
                        content_dir_matrix_path(user_home()),
                        content_dir_path(user_home())
                    ),
                    cp(
                        content_dir_matrix_path_php(user_home()),
                        content_dir_path(user_home())
                    ),
                    wget(apache_download, destination=(home + "/")),
                    extract(apache_extract, destination=home),
                    cd(apache_extracted),
                    "./configure --prefix=" + apache_home,
                    "make",
                    "make install",
                    cd("~"),
                    rm(apache_extracted),
                    rm(apache_tar_gz)
                )
            ),
            cd(home + "/" + apache_factory),
            python(brotli_installation_script, account),
            run_as_user(
                account,
                concatenate(
                    cd(user_home() + "/" + apache_factory),
                    python(password_protect_script),
                    python(mysql_installation_script, account),
                    python(php_installation_script, account),
                    python(distribution_script)
                )
            )
        )
    )
]

run(steps)
