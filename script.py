import os
from diagrams import Diagram
from diagrams.custom import Custom

ROOT_DIR = ''

def store_directories(rootdir):
    directories = []
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        if os.path.isdir(path) and "node_modules" not in path and ".git" not in path:
            folders = path[start:].split(os.sep)
            directories.append(folders)
    return directories        

directories = store_directories(ROOT_DIR)
nodes = []
with Diagram("Name", show=False, filename="room", direction="TB"):
    for index, directorie in enumerate(directories):
        nodes.append(Custom(directorie[len(directorie) - 1], "./blankYellowFolder.svg"))
    
    
    for index, node in enumerate(nodes):
        if index != 0:
            parent_label = directories[index][len(directories[index]) - 2]
            parent_node = [n for n in nodes if n.label == parent_label]

            parent_node[0] >> node