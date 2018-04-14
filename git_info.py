import subprocess
from configuration import *


def set_git_info():
    star = "* "
    fetch_url = "Fetch URL:"
    url_result = subprocess.check_output(["git", "remote", "show", "origin"])
    branch_result = subprocess.check_output(["git", "branch"])
    url_split_result = str(url_result).split("\\n")
    branch_split_result = str(branch_result).split("\\n")

    for line in url_split_result:
        if fetch_url in str(line):
            repository = str(line).replace(fetch_url, "").strip()
            print("Repository is: " + repository)
            break

    for line in branch_split_result:
        if "* " in str(line):
            branch = str(line)[str(line).index(star) + star.__len__():].strip()
            print("Branch is: " + branch)
            break
