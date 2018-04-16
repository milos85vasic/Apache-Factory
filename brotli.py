import sys
from commands import *
from configuration import *
from system_configuration import *

account = sys.argv[1]

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
    concatenate(
        cd(get_home_directory_path(account)),
        mkdir(brotli_module),
        cd(brotli_module),
        "git clone --depth=1 --recursive " + brotli_module_repository + " ./",
        "./autogen.sh",
        "./configure",
        "make",
        "install -p -m 755 -D .libs/mod_brotli.so " + apache_home + "/modules/mod_brotli.so"
    )
]

run(steps)
