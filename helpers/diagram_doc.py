# Module to create diagrams from a source

from diagrams import Diagram
from diagrams.custom import Custom

nodes = []

# Create a tree diagrams to see folder structure as a tree
def folder_structure_diagram(directories, name, file_name):
    with Diagram(name, show=False, filename=file_name, direction="TB"):
        for index, directorie in enumerate(directories):
            nodes.append(Custom(directorie[len(directorie) - 1], "assets/folder.svg"))
        
        
        for index, node in enumerate(nodes):
            if index != 0:
                parent_label = directories[index][len(directories[index]) - 2]
                parent_node = [n for n in nodes if n.label == parent_label]

                parent_node[0] >> node
