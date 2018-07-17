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
            "service webmin start",
            "/root/" + apache_factory + "/" + starter_script
        )
    )
]

run(commands)

