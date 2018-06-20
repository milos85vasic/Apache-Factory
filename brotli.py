import sys
from Toolkit.commands import *
from configuration import *
from Toolkit.system_configuration import *

account = sys.argv[1]


def user_home():
    return get_home_directory_path(account)


steps = [
    concatenate(
        cd(get_home_directory_path(account)),
        mkdir(brotli),
        cd(brotli),
        git_clone_to(brotli_repository, "./"),
        "mkdir out && cd out",
        "../configure-cmake",
        "make",
        "make test",
        "make install"
    ),
    run_as_user(
        account,
        concatenate(
            cd(user_home()),
            mkdir(brotli_module),
            cd(brotli_module),
            "git clone --depth=1 --recursive " + brotli_module_repository + " ./",
            "./autogen.sh",
            "./configure",
            "make",
            "install -p -m 755 -D .libs/mod_brotli.so " + user_home() + "/" + apache2 + "/modules/mod_brotli.so"
        )
    )
]

run(steps)
