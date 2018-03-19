import sys
from commands import *

account = ""

for arg in sys.argv:
    if sys.argv.index(arg) > 0:
        account += arg

steps = [
    cd("~"),
    clear(),
    echo("Creating account: " + account)
]

run(steps)
