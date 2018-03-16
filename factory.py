import os
from os.path import expanduser

home = expanduser("~")

apacheHome = home + "/Apache2"

steps = [
    "mkdir " + apacheHome
]

for step in steps:
    os.system(step)
