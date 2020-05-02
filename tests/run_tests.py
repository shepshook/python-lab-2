import unittest
from . import test_vector_class
from . import test_sort_class
from . import test_json_class


def main():
    suite_vector = unittest.TestLoader().loadTestsFromModule(test_vector_class)
    suite_sort = unittest.TestLoader().loadTestsFromModule(test_sort_class)
    suite_json = unittest.TestLoader().loadTestsFromModule(test_json_class)
    all_tests = unittest.TestSuite([suite_vector, suite_sort, suite_json])
    unittest.TextTestRunner(verbosity=2).run(all_tests)
    pass
