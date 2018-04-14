import subprocess
from configuration import *

branch = "master"

fetch_url = "Fetch URL:"
result = subprocess.check_output(["git", "remote", "show", "origin"])
split_result = str(result).split("\\n")

for line in split_result:
    if fetch_url in str(line):
        repository = str(line).replace(fetch_url, "").strip()
        print("Repository is: " + repository)
        print("Branch is: " + branch)
        break
