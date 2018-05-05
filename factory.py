import getpass
from commands import *
from configuration import *

account = getpass.getuser()


def user_home():
    return get_home_directory_path(account)


steps = [
    clear(),
    run_as_su(
        concatenate(
            get_yum_group("Development Tools"),
            get_yum("openssl-devel"),
            get_yum("gcc"),
            get_yum("make"),
            get_yum("cmake"),
            get_yum("automake"),
            get_yum("libtool"),
            get_yum("apr-devel"),
            get_yum("apr-util-devel"),
            get_yum("wget"),
            get_yum("git"),
            get_yum("sqlite"),
            get_yum("libxml2"),
            get_yum("libxml2-devel"),
            add_to_group(account, apache_factory_group),
            mkdir(content_dir_path(user_home())),
            chown(account, content_dir_path(user_home())),
            chgrp(account, content_dir_path(user_home())),
            run_as_user(
                account,
                concatenate(
                    clear(),
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
                    clear(),
                    extract(apache_extract, destination=home),
                    clear(),
                    cd(apache_extracted),
                    "./configure --prefix=" + apache_home,
                    "make",
                    "make install",
                    cd("~"),
                    clear(),
                    rm(apache_extracted)
                )
            ),
            cd(home + "/" + apache_factory),
            python(brotli_installation_script, account),
            run_as_user(
                account,
                concatenate(
                    cd(user_home() + "/" + apache_factory),
                    python(mysql_installation_script, account),
                    python(php_installation_script, account),
                    python(distribution_script)
                )
            )
        )
    )
]

run(steps)
