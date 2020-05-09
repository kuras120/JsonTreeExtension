from enum import Enum
from typing import List
from treelib import Node, Tree


class FileMode(Enum):
    BASIC = 1
    EXTENDED = 2


class FileWriter:
    def __init__(self, file):
        self.__file = file

    # parent, siblings (rodzenstwo), paths_to_leaves
    def write(self, tree: Tree):
        opened = open(self.__file, 'w+')
        paths: list = tree.paths_to_leaves()
        for elem in paths:
            node: Node = tree.get_node(elem[-1])
            parent: Node = tree.get_node(elem[-2])
            opened.write(parent.tag + ': ' + node.tag + '\n')
        opened.close()
