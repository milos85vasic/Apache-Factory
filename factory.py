import os
from os.path import expanduser

home = expanduser("~")

apacheHome = home + "/Apache2"
apacheTarBz = "httpd-2.4.29.tar.gz"
apacheDownload = "http://www-us.apache.org/dist//httpd/" + apacheTarBz

steps = [
    "clear",
    "echo 'Installing dependencies'",
    "yum install -y openssl-devel",
    'yum install group -y "Development Tools"',
    "clear",
    # "yum install -y ", TODO: Add APR dependency
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
    "echo 'Configuring build'",
    home + "/" + apacheTarBz.replace(".tar.gz", "") + "/configure --prefix=" + apacheHome
]

for step in steps:
    os.system(step)
