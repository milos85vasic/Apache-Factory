#!/usr/bin/python
import getpass
import sys

from Toolkit.commands import *
from Toolkit.system_configuration import *
from configuration import *

account = getpass.getuser()
certbot_command = sys.argv[1]

print("Certbot command: " + certbot_command)

if account is "root":
    print "Only super user can trigger certbot renew."
    sys.exit(2)

# TODO: This paths should be relative.
commands = [
    python(
        "/root/" + apache_factory + "/" + killer_script,
        "root",
        "pserve",
        "--all"
    ),
    python(
        "/root/" + apache_factory + "/" + killer_script,
        "root",
        "httpd",
        "--all"
    ),
    python(
        "/root/" + apache_factory + "/" + killer_script,
        "root",
        "mysqld",
        "--all"
    ),
    "service webmin stop",
    certbot_command,
    "service webmin start"
]

apache_start_script = "/root/" + apache_factory + "/" + starter_script
pyramid_start_script = "/root/" + pyramid_factory + "/" + starter_script_py

if os.path.isfile(apache_start_script):
    commands.append(python(apache_start_script))

if os.path.isfile(pyramid_start_script):
    commands.append(python(pyramid_start_script))

run(commands)
