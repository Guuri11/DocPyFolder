import os
import json

from helpers.markdown_doc import package_json_md

def scan(rootdir):
    directories = []
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        if os.path.isdir(path) and "node_modules" not in path and ".git" not in path:
            if "package.json" in files:
                package_json = path + "/" + "package.json"
                text_file = open(package_json, "r")
                data = text_file.read()
                package_json_md(json.loads(data), "File Name", "Title of project")
                text_file.close()
            folders = path[start:].split(os.sep)
            directories.append(folders)
    return directories