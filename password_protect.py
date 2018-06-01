import getpass

from commands import *
from configuration import *
from system_configuration import *

account = getpass.getuser()

system_configuration = get_system_configuration()

if key_password_protect in system_configuration:
    for password_protect in system_configuration[key_password_protect]:
        print(
            "We are about to initialize file user with credentials [ " +
            password_protect[key_password_protect_user] + " ][ " + password_protect[key_password_protect_password] +
            " ]"
        )
