from commands import *
from configuration import *

steps = [
    cd(home),
    mkdir(brotli),
    cd(brotli),
    git_clone_to(brotli_repository, "./"),
    "mkdir out && cd out",
    "../configure-cmake",
    "make",
    "make test",
    "make install",
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