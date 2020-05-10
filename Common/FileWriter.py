from enum import Enum
from typing import List
from treelib import Node, Tree


class FileMode(Enum):
    BASIC = 1
    EXTENDED = 2


class FileWriter:
    def __init__(self, file, mode: FileMode = FileMode.BASIC):
        self.__file = file
        self.__mode = mode

    # parent, siblings (rodzenstwo), paths_to_leaves
    def write(self, tree: Tree):
        opened = open(self.__file, 'w+')
        paths: List = tree.paths_to_leaves()
        if self.__mode == FileMode.BASIC:
            for elem in paths:
                node: Node = tree.get_node(elem[-1])
                parent: Node = tree.get_node(elem[-2])
                opened.write(parent.tag + ': ' + node.tag + '\n')
        elif self.__mode == FileMode.EXTENDED:
            visited_paths = []
            for elem in paths:
                parent: Node = tree.get_node(elem[-2])
                if parent.identifier not in visited_paths:
                    nodes: List[Node] = tree.children(parent.identifier)
                    tags: List[str] = []
                    for node in nodes:
                        tags.append(node.tag)
                    opened.write(parent.tag + ': ' + str(tags).replace('[', '')
                                 .replace('\'', '').replace(']', '') + '\n')
                    visited_paths.append(parent.identifier)
        opened.close()
