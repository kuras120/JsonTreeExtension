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
        nodes: List[Node] = tree.leaves('root')
        print(nodes)
        print(nodes[0])
        parent: Node = tree.parent(nodes[0].identifier)
        print(parent)
        paths: list = tree.paths_to_leaves()
        print(paths)
