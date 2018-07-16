#!/usr/bin/python
import sys

from Toolkit.commands import *
from Toolkit.system_configuration import *
from configuration import *

certbot_command = sys.argv[1]

commands = [
    run_as_su(
        concatenate(
            python(
                killer_script,
                "root",
                "httpd"
            ),
            "service webmin stop",
            certbot_command,
            "service webmin start",
            starter_script
        )
    )
]

run(commands)

