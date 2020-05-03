import unittest
import pyson


class TestPyson(unittest.TestCase):
    def setUp(self):
        class NestedClass:
            def __init__(self):
                self.tup = (1, (2, 3))

        class TestClass:
            def __init__(self):
                self.s = "zen of python"
                self.l = [1, 2, 5]
                self.n = 123
                self.t = (3, 4, 5)
                self.d = {"a": 1, "b": 4}
                self.b = False
                self.c = NestedClass()

        self.test_instance = TestClass()

    def test_pyson_serialize(self):
        expected = \
            '{"s":"zenofpython","l":[1,2,5],"n":123,"t":[3,4,5],"d":{"a":1,"b":4},"b":False,"c":{"tup":[1,[2,3]]}}'
        result = pyson.serialize(self.test_instance)
        self.assertTrue(expected == "".join(result.split()))
