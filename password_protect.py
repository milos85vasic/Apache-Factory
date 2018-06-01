import getpass

from commands import *
from configuration import *
from system_configuration import *

account = getpass.getuser()

system_configuration = get_system_configuration()

print(system_configuration)

if account in system_configuration:
    if key_services in system_configuration[account]:
        if key_password_protect in system_configuration[account]:
            for password_protect in system_configuration[key_password_protect]:
                print(
                    "We are about to initialize file user with credentials [ " +
                    password_protect[key_password_protect_user] + " ][ " + password_protect[
                        key_password_protect_password] +
                    " ]"
                )
