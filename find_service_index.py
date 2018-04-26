import json
import getpass
import sys

from commands import *
from configuration import *
from system_configuration import *

account = getpass.getuser()

system_configuration = get_system_configuration()

service_name = sys.argv[1]
service_home = sys.argv[2]
service = system_configuration[account][service_name]



