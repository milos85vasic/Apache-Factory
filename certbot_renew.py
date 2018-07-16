#!/usr/bin/python
import sys

from Toolkit.commands import *
from Toolkit.system_configuration import *
from configuration import *

certbot_command = sys.argv[1]

commands = [
    run_as_su(
        concatenate(
            # TODO: Make sure it is possible to kill for all users.
            python(
                killer_script,
                "root",
                "httpd"
            ),
            "service webmin stop",
            certbot_command,
            "service webmin start",
            "/root/" + apache_factory + "/" + starter_script
        )
    )
]

run(commands)

