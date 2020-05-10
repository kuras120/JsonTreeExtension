import unittest2


class MyTestCase(unittest2.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest2.main()
