from commands import *
from distribution_utils import *

steps = [
    curl("http://localhost:" + get_port())
]

run(steps)
