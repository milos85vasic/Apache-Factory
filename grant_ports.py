import sys

from commands import *

path_to_binary = sys.argv[1]

if path_to_binary:
    steps = [
        run_as_su(
            "setcap CAP_NET_BIND_SERVICE=+eip " + path_to_binary
        )
    ]

    run(steps)
