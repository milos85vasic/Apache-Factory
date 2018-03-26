from configuration import *


def get_port():
    prefix = "Listen "
    with open(apache_conf + "/" + httpd_conf, "rt") as fin:
        for line in fin:
            if line.startswith(prefix):
                port = line.replace(prefix, "")
                print "Apache will listen at port: " + port
                return port
    return "8080"
