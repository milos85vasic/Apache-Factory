import sys
from commands import *
from configuration import *

account = ""

for arg in sys.argv:
    if sys.argv.index(arg) > 0:
        account += arg

steps = [
    run_as_su(
        concatenate(
            cd("~"),
            clear(),
            add_user(account),
            passwd(account),
            add_group(apache_factory_group),
            # TODO: Prepare /usr/share directory.
            clear()
        )
    ),
    run_as_user(
        account,
        concatenate(
            mkdir(apache_factory),
            cd(apache_factory),
            git_clone(repository),
            python(factory_script)
        )
    )
]
run(steps)
