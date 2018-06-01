import getpass

from commands import *
from configuration import *
from system_configuration import *

account = getpass.getuser()

system_configuration = get_system_configuration()

print(account)
print(system_configuration)

if account in system_configuration:
    print("Ok 1")
    if key_services in system_configuration[account]:
        print("Ok 1")
        if key_password_protect in system_configuration[account][key_services]:
            print("Ok 2")
            for password_protect in system_configuration[account][key_services][key_password_protect]:
                print(
                    "We are about to initialize file user with credentials [ " +
                    password_protect[key_password_protect_user] + " ][ " + password_protect[
                        key_password_protect_password] +
                    " ]"
                )
