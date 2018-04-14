import subprocess
import json

key_branch = "branch"
destination = "git_info.json"
key_repository = "repository"


def set_git_info():
    star = "* "
    branch = ""
    repository = ""
    fetch_url = "Fetch URL:"
    url_result = subprocess.check_output(["git", "remote", "show", "origin"])
    branch_result = subprocess.check_output(["git", "branch"])
    url_split_result = str(url_result).split("\\n")
    branch_split_result = str(branch_result).split("\\n")

    for line in url_split_result:
        if fetch_url in str(line):
            repository = str(line).replace(fetch_url, "").strip()
            break

    for line in branch_split_result:
        if "* " in str(line):
            branch = str(line)[str(line).index(star) + star.__len__():].strip()
            break

    git_configuration = {
        key_branch: branch,
        key_repository: repository
    }

    print("Repository is: " + git_configuration[key_repository])
    print("Branch is: " + git_configuration[key_branch])

    try:
        with open(destination, 'w') as outfile:
            json.dump(git_configuration, outfile)
    except IOError:
        print("Can't access " + destination)


def get_git_info():
    return json.load(open(destination))


set_git_info()
