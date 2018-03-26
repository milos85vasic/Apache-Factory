from configuration import *


def get_port():
    prefix = "Listen "
    path = apache_conf + "/" + httpd_conf
    print "Parsing for port number: " + path
    with open(path, "rt") as fin:
        for line in fin:
            if prefix in line:
                port = line.replace(prefix, "")
                print "Apache will listen at port: " + port
                return str(port)
    return "8080"
