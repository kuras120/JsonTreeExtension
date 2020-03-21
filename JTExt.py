from treelib import Node, Tree


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

    def parse_json(self, json_dict: dict, key: str = 'root') -> None:
        for k in json_dict.keys():
            if isinstance(json_dict[k], dict):
                self.__tree.create_node(str(k).upper(), k, parent=key)
                self.parse_json(json_dict[k], k)
            elif isinstance(json_dict[k], list):
                for item in json_dict[k]:
                    if isinstance(item, dict):
                        self.__tree.create_node(str(k).upper(), k, parent=key)
                        self.parse_json(item, k)
                    else:
                        self.__tree.create_node(str(k).upper(), k, parent=key, data=item)
            else:
                self.__tree.create_node(str(k).upper(), k, parent=key, data=json_dict[k])
