#!/usr/bin/env python3
import constants as c
from helpers.diagram_doc import folder_structure_diagram
from helpers.markdown_doc import package_json_md
import helpers.project_scan as pscan

def run():
    print("Running process...")
    directories = pscan.scan(c.ROOT_DIR)
    folder_structure_diagram(directories, "Project name", "File name")

if __name__ == "__main__":
    run()