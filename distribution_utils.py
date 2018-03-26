from configuration import *


def get_port():
    port = "8080"
    prefix = "Listen "
    path = apache_conf + "/" + httpd_conf
    print "Parsing for port number: " + path
    with open(path, "rt") as fin:
        for line in fin:
            print line
            if prefix in line:
                port = line.replace(prefix, "")
                print "Apache will listen at port: " + port
                return str(port)
    return port
