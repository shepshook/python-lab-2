import unittest
from . import test_vector_class
from . import test_sort_class
from . import test_json_class
from . import test_cached_decorator


def main():
    suite_vector = unittest.TestLoader().loadTestsFromModule(test_vector_class)
    suite_sort = unittest.TestLoader().loadTestsFromModule(test_sort_class)
    suite_json = unittest.TestLoader().loadTestsFromModule(test_json_class)
    suite_cached = unittest.TestLoader().loadTestsFromModule(test_cached_decorator)
    all_tests = unittest.TestSuite([suite_vector, suite_sort, suite_json, suite_cached])
    unittest.TextTestRunner(verbosity=2).run(all_tests)
    pass
