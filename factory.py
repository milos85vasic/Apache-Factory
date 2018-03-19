import os
from os.path import expanduser

home = expanduser("~")

apacheHome = home + "/Apache2"
apacheTarBz = "httpd-2.4.29.tar.gz"
apacheDownload = "http://www-us.apache.org/dist//httpd/" + apacheTarBz


def get_su(what):
    return "su -c '" + what + "'"


def get_yum(what):
    return "yum install -y " + what


def get_yum_group(what):
    return "yum install group -y '" + what + "'"


def concatenate(*what):
    result = ""
    for item in what:
        result += " " + item + ";"


steps = [
    "clear",
    "echo 'Installing dependencies'",
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
    "clear",
    "echo 'Making Apache home directory'",
    "mkdir " + apacheHome,
    "echo 'Downloading Apache'",
    "wget " + apacheDownload + " -P " + apacheHome + "/",
    "clear",
    "echo 'Extracting Apache'",
    "tar  -xvzf " + apacheHome + "/" + apacheTarBz + " --directory " + home,
    "clear",
    "echo 'Apache installation extracted'\n"
    "echo 'Configuring Apache build'",
    home + "/" + apacheTarBz.replace(".tar.gz", "") + "/configure --prefix=" + apacheHome,
    "clear",
    "echo 'Making Apache build'",
]

for step in steps:
    os.system(step)
