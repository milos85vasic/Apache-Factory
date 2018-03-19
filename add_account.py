import sys
from commands import *

account = ""
factory_script = "factory.py"
apache_factory = "Apache-Factory"
repository = "https://github.com/milos85vasic/Apache-Factory.git"

for arg in sys.argv:
    if sys.argv.index(arg) > 0:
        account += arg

steps = [
    cd("~"),
    clear(),
    echo("Creating account: " + account),
    add_user(account),
    passwd(account),
    clear(),
    echo("Starting Apache Factory for the account: " + account),
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
