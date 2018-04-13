import getpass
from commands import *
from configuration import *

account = getpass.getuser()

steps = [
    cd("~"),
    clear(),
    run_as_su(
        concatenate(
            get_yum_group("Development Tools"),
            get_yum("openssl-devel"),
            get_yum("gcc"),
            get_yum("make"),
            get_yum("apr-devel"),
            get_yum("apr-util-devel"),
            get_yum("wget"),
            get_yum("git"),
            add_to_group(account, apache_factory_group),
            run_as_user(
                account,
                concatenate(
                    clear(),
                    mkdir(apache_home),
                    mkdir(content_dir_path),
                    cp(
                        content_dir_matrix_path(get_home_directory_path(account)),
                        content_dir_path(get_home_directory_path(account))
                    ),
                    # wget(apache_download, destination=(home + "/")),
                    # clear(),
                    # extract(apache_extract, destination=home),
                    # clear(),
                    # cd(apache_extracted),
                    # "./configure --prefix=" + apache_home,
                    # "make",
                    # "make install",
                    # cd("~"),
                    # clear(),
                    # rm(apache_extracted),
                    # cd(apache_factory_full_path(account)),
                    # python(distribution_script)
                )
            )
        )
    )
]

run(steps)
