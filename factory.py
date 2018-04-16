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
            # get_yum_group("Development Tools"),
            # get_yum("openssl-devel"),
            # get_yum("gcc"),
            # get_yum("make"),
            # get_yum("cmake"),
            # get_yum("automake"),
            # get_yum("libtool"),
            # get_yum("apr-devel"),
            # get_yum("apr-util-devel"),
            # get_yum("wget"),
            # get_yum("git"),
            get_yum("httpd-devel"),
            add_to_group(account, apache_factory_group),
            run_as_user(
                account,
                concatenate(
                    clear(),
                    cd("~"),
                    # mkdir(apache_home),
                    # mkdir(content_dir_path(user_home())),
                    # cp(
                    #     content_dir_matrix_path(user_home()),
                    #     content_dir_path(user_home())
                    # ),
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
                    python(brotli_installation_script),
                    # cd(user_home() + "/" + apache_factory),
                    # python(distribution_script)
                )
            )
        )
    )
]

run(steps)
