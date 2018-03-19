import os
from os.path import expanduser

home = expanduser("~")


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
    return result


def echo(*what):
    for item in what:
        print item
    return ""


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


def cd(where):
    return "cd " + where


def run(what):
    for cmd in what:
        os.system(cmd)


def add_user(user):
    return "adduser " + user


def passwd(user):
    return "passwd " + user


def run_as_user(account, command):
    return "sudo -H -u " + account + " bash -c '" + command + "'"


def git_clone(what):
    return "git clone " + what


def python(script):
    return "python " + script