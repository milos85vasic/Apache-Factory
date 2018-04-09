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
                    cp(content_dir_matrix_path, content_dir_path),  # FIXME: It does not copy the file.
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
                    rm(apache_extracted),
                    cd(apache_factory_full_path),
                    python(distribution_script)
                )
            )
        )
    )
]

run(steps)
