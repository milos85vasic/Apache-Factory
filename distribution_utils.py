from configuration import *


def get_port():
    return str(7777)
    # prefix = "Listen "
    # path = apache_conf + "/" + httpd_conf
    # print "Parsing for port number: " + path
    # with open(path, "rt") as fin:
    #     for line in fin:
    #         if line.startswith(prefix):
    #             port = line.replace(prefix, "")
    #             print "Apache will listen at port: " + port
    #             return port
    # return "8080"
