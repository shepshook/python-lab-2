import unittest
import cached_decorator


class TestCachedDecorator(unittest.TestCase):
    def setUp(self):
        class CountedDict(dict):
            def __init__(self, *args):
                dict.__init__(self, args)
                self.sets_count = 0
                self.gets_count = 0

            def __setitem__(self, key, value):
                dict.__setitem__(self, key, value)
                self.sets_count += 1

            def __getitem__(self, key):
                value = dict.__getitem__(self, key)
                self.gets_count += 1
                return value

        self.cache = CountedDict()

        @cached_decorator.cached(self.cache)
        def foo(x):
            if x == "bar":
                return "foobar"
            else:
                return "fizzbuzz"
        self.foo = foo

    def test_cache_decorator_same_data(self):
        for _ in range(10):
            self.foo("bar")
        self.assertTrue(self.cache.sets_count == 1, self.cache.gets_count == 9)

    def test_cache_decorator_various_data(self):
        for a in "foobar":
            self.foo(a)
        self.assertTrue(self.cache.sets_count == 5, self.cache.gets_count == 1)