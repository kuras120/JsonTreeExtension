import unittest
from typing import List
from treelib import Tree
from Core.JTExt import JTExt


class JTExtUnitTest(unittest.TestCase):
    def test_parse_json_basic(self):
        parser = JTExt()
        tree: Tree = parser.parse_json({"test": "true", "test2": {"test3": "false", "test4": ["true", "false", "true"]}})
        leaves: List = tree.paths_to_leaves()
        test_list: List = [["ROOT", "TEST", "TRUE"],
                           ["ROOT", "TEST2", "TEST3", "FALSE"],
                           ["ROOT", "TEST2", "TEST4", "TRUE"],
                           ["ROOT", "TEST2", "TEST4", "FALSE"],
                           ["ROOT", "TEST2", "TEST4", "TRUE"]]
        for i in range(len(test_list)):
            for j in range(len(test_list[i])):
                self.assertEqual(tree.get_node(leaves[i][j]).tag, test_list[i][j])


if __name__ == '__main__':
    unittest.main()
