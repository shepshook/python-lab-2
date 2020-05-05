import unittest
import cached_decorator


class TestCachedDecorator(unittest.TestCase):
    def setUp(self):
        self.real_calls_count = 0

        @cached_decorator.cached
        def foo(a, b):
            self.real_calls_count += 1
            return a + b
        self.foo = foo

    def test_cache_decorator_same_data(self):
        for _ in range(10):
            self.foo(1, 2)
        self.assertTrue(self.real_calls_count == 1)

    def test_cache_decorator_various_kwargs_order(self):
        self.foo(a=1, b=2)
        self.foo(b=2, a=1)
        self.foo(a=1, b=2)
        self.assertTrue(self.real_calls_count == 1)
