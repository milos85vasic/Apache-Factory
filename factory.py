import os
from os.path import expanduser

home = expanduser("~")

apacheHome = home + "/Apache2"
apacheTarBz = "httpd-2.4.29.tar.gz"
apacheDownload = "http://www-us.apache.org/dist//httpd/" + apacheTarBz

steps = [
    "clear",
    "echo 'Installing dependencies'"
    'yum install group -y "Development Tools"',
    "clear",
    "echo 'Making Apache home directory'",
    "mkdir " + apacheHome,
    "echo 'Downloading Apache'",
    "wget " + apacheDownload + " -P " + apacheHome + "/",
    "clear",
    "echo 'Extracting Apache'",
    "tar  -xvzf " + apacheHome + "/" + apacheTarBz + " --directory " + home,
    "clear",
    "echo 'Apache installation extracted'"
]

for step in steps:
    os.system(step)
