import os
from os.path import expanduser

home = expanduser("~")

apacheHome = home + "/Apache2"
apacheTarBz = "httpd-2.4.29.tar.gz"
apacheDownload = "http://www-us.apache.org/dist//httpd/" + apacheTarBz

steps = [
    "mkdir " + apacheHome,
    "wget " + apacheDownload + " -P " + apacheHome + "/"
]

for step in steps:
    os.system(step)
