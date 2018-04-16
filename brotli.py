import getpass
from commands import *
from configuration import *

account = getpass.getuser()

steps = [
    cd("~"),
    mkdir(brotli),
    cd(brotli),
    git_clone_to(brotli_repository, "./"),
    "mkdir out && cd out",
    "../configure-cmake",
    "make",
    "make test",
    run_as_su("make install"),
    cd("~"),
    mkdir(brotli_module),
    cd(brotli_module),
    "git clone --depth=1 --recursive " + brotli_module_repository + " ./",
    "./autogen.sh",
    "./configure",
    "make",
    "install -p -m 755 -D .libs/mod_brotli.so " + apache_home + "/modules/mod_brotli.so"
]

run(steps)
