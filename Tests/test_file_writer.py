import io
import unittest
from treelib import Tree
from Core.JTExt import JTExt
from Common.FileWriter import FileWriter, FileMode


class FileWriterUnitTest(unittest.TestCase):
    def test_parser_basic(self):
        parser = JTExt()
        tree: Tree = parser.parse_json({"test": "true", "test2": {"test3": "false", "test4": ["true", "false", "true"]}})
        writer = FileWriter("Files/TestBasicNew.txt")
        writer.write(tree)
        file1 = io.open("Files/TestBasic.txt")
        file2 = io.open("Files/TestBasicNew.txt")
        self.assertListEqual(list(file1), list(file2))
        file1.close()
        file2.close()

    def test_parser_extended(self):
        parser = JTExt()
        tree: Tree = parser.parse_json({"test": "true", "test2": {"test3": "false", "test4": ["true", "false", "true"]}})
        writer = FileWriter("Files/TestExtendedNew.txt", FileMode.EXTENDED)
        writer.write(tree)
        file1 = io.open("Files/TestExtended.txt")
        file2 = io.open("Files/TestExtendedNew.txt")
        self.assertListEqual(list(file1), list(file2))
        file1.close()
        file2.close()


if __name__ == '__main__':
    unittest.main()
