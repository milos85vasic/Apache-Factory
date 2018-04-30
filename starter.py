import sys
from commands import *
from system_configuration import *
from configuration import *
from git_info import *

system_configuration = get_system_configuration()

for item in system_configuration.keys():
    account = item
    script = get_home_directory_path(account)
    script += "/" + apache2 + "/bin/apachectl"
    if os.path.isfile(script):
        steps = [
            run_as_user(
                account,
                python(script, "start")
            )
        ]

        run(steps)
