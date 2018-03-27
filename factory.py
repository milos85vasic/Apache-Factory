from commands import *
from configuration import *

steps = [
    cd("~"),
    clear(),
    echo("Installing dependencies"),
    run_as_su(
        concatenate(
            get_yum_group("Development Tools"),
            get_yum("openssl-devel"),
            get_yum("gcc"),
            get_yum("make"),
            get_yum("apr-devel"),
            get_yum("apr-util-devel"),
            get_yum("wget"),
            get_yum("git")
        )
    ),
    clear(),
    echo("Making Apache home directory"),
    mkdir(apache_home),
    echo("Downloading Apache"),
    wget(apache_download, destination=(home + "/")),
    clear(),
    echo("Extracting Apache"),
    extract(apache_extract, destination=home),
    clear(),
    echo("Apache installation extracted", "Making Apache build"),
    concatenate(
        cd(apache_extracted),
        "./configure --prefix=" + apache_home,
        "make",
        "make install",
        cd("~")
    ),
    clear(),
    echo("Apache build made"),
    rm(apache_extracted),
    python(distribution_script)
]

run(steps)
