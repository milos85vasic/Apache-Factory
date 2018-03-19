from commands import *

steps = [
    clear(),
    echo("Installing dependencies"),
    get_su(
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
    mkdir(apacheHome),
    echo("Downloading Apache"),
    wget(apacheDownload, destination=(apacheHome + "/")),
    clear(),
    echo("Extracting Apache"),
    extract(apacheHome + "/" + apacheTarBz, destination=home),
    clear(),
    echo("Apache installation extracted", "Making Apache build"),
    concatenate(
        cd(home + "/" + apacheTarBz.replace(".tar.gz", "")),
        "./configure --prefix=" + apacheHome,
        "make",
        "make install",
        cd("~")
    ),
    clear(),
    echo("Apache build made")
]

run(steps)
