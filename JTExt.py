import json
import uuid
import string
import random
from typing import TypeVar
from treelib import Node, Tree

JsonDictType = TypeVar('JsonDictType', dict, list, str)


class JTExt:
    def __init__(self, tree: Tree = None):
        if tree:
            self.__tree = tree
        else:
            self.__tree = Tree()
        self.__tree.create_node('ROOT', 'root')

    def get_parent(self) -> Node:
        pass

    def get_children(self) -> list:
        pass

    def parse_json(self, json_dict: JsonDictType, key: str = 'root') -> Tree:
        if isinstance(json_dict, str):
            json_dict = json.loads(json_dict)

        if isinstance(json_dict, dict):
            iteration_data = json_dict.keys()
        elif isinstance(json_dict, list):
            iteration_data = json_dict
        else:
            self.__tree.create_node(str(json_dict).upper(), json_dict, parent=key)
            return self.__tree

        for k in iteration_data:
            identifier = uuid.uuid1()
            if isinstance(json_dict[k], dict):
                self.__tree.create_node(str(k).upper(), str(identifier), parent=key)
                self.parse_json(json_dict[k], str(identifier))
            elif isinstance(json_dict[k], list):
                self.__tree.create_node(str(k).upper(), str(identifier), parent=key)
                for item in json_dict[k]:
                    if isinstance(item, dict) or isinstance(item, list):
                        self.parse_json(item, str(identifier))
                        identifier = uuid.uuid1()
                    else:
                        self.__tree.create_node(str(item).upper(), parent=str(identifier))
            else:
                self.__tree.create_node(str(k).upper(), str(identifier), parent=key)
                self.__tree.create_node(str(json_dict[k]).upper(), parent=str(identifier))
        return self.__tree

    # ----------------------- UTILS ----------------------- #
    @staticmethod
    def random_string(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    @staticmethod
    def generate_test_json(elements=3) -> str:
        data = {}
        for _ in range(elements):
            data[JTExt.random_string()] = {JTExt.random_string(): [JTExt.random_string() for _ in range(elements)],
                                           JTExt.random_string(): {JTExt.random_string(): 5,
                                                                   JTExt.random_string(): {JTExt.random_string(): 3,
                                                                                           JTExt.random_string(): [5, 2, 7]}}}
        return json.dumps(data)


if __name__ == '__main__':
    parser = JTExt()
    prob = JTExt.generate_test_json()
    print(prob)
    tree = parser.parse_json(prob)
    tree.show()
