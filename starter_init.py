import sys
from commands import *
from configuration import *

if os.path.isfile(rc_local):
    abs_pth = os.path.abspath('')
    script = abs_pth + "/" + starter_script
    if script not in open(rc_local).read():
        with open(rc_local, "a") as rc:
            rc.write(script)

    steps = [
        chmodx(rc_local)
    ]

    run(steps)
