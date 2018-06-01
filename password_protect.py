import getpass

from commands import *
from configuration import *
from system_configuration import *

account = getpass.getuser()

system_configuration = get_system_configuration()

if account in system_configuration:
    if key_services in system_configuration[account]:
        if key_password_protect in system_configuration[account][key_services]:
            for password_protect in system_configuration[account][key_services][key_password_protect]:
                print(
                    "We are about to initialize file user with credentials [ " +
                    password_protect[key_password_protect_user] + " ][ " + password_protect[
                        key_password_protect_password] +
                    " ]"
                )

                cmd = get_home_directory_path(account) + "/" + apache2 + "/bin/htpasswd"
                passwd_file_path = get_home_directory_path(account) + "/" + security + "/" + passwd_file

                append = passwd_file_path + " " + password_protect[key_password_protect_user] + " " + password_protect[
                    key_password_protect_password
                ]

                if os.path.isfile(passwd_file_path):
                    cmd += " " + append
                else:
                    cmd += " -c " + append

                steps = [
                    mkdir(get_home_directory_path(account) + "/" + security),

                ]

                run(steps)
