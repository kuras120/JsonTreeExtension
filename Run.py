from Core.JTExt import JTExt
from Common.FileWriter import FileWriter, FileMode


if __name__ == '__main__':
    if __name__ == '__main__':
        parser = JTExt()
        prob = JTExt.generate_test_json()
        tr3 = parser.parse_json(prob)
        tr3.show()
        writer = FileWriter('file.txt', FileMode.EXTENDED)
        writer.write(tr3)
