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


def echo(*what):
    result = ""
    for item in what:
        result += item + '\n'
    return "echo '" + result + "'"


def clear():
    return "clear"


def wget(what, **params):
    destination = 'destination'
    if destination in params:
        return wget(what) + " -P " + params[destination]
    else:
        return "wget " + what


def mkdir(dir_name):
    return "mkdir " + dir_name


def extract(what, **params):
    destination = 'destination'
    if destination in params:
        return "tar  -xvzf " + what + " --directory " + params[destination]
    else:
        return "tar  -xvzf " + what


def run(*what):
    for cmd in what:
        os.system(cmd)


def cd(where):
    return "cd " + where
