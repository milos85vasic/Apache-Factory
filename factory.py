import os

apacheHome = "Apache2"

steps = [
    "mkdir " + apacheHome
]

for step in steps:
    os.system(step)
