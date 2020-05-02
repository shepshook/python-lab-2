import unittest
from .. import external_sort, create_large_file
import os, time


class TestExternalSortResult(unittest.TestCase):
    def setUp(self):
        create_large_file.create_file("numbers.txt", 1000)

    def test_external_sort_result(self):
        external_sort.sort("numbers.txt", "sorted.txt", 50)
        self.assertTrue(self.file_sorted())

    def file_sorted(self):
        with open("sorted.txt", 'r') as file:
            a = int(file.readline())
            b = int(file.readline())
            while True:
                if b:
                    if a > b:
                        return False
                    a = b
                    b = int(file.readline())
                else:
                    break
            return True

    def tearDown(self):
        os.remove("numbers.txt")
        os.remove("sorted.txt")


class TestExternalSortPerformance(unittest.TestCase):
    def setUp(self):
        create_large_file.create_file("numbers.txt", 100000)
        self.start_time = time.time()

    def test_external_sort_performance(self):
        external_sort.sort("numbers.txt", "sorted.txt")

    def tearDown(self):
        print(f"Sorted in {time.time() - self.start_time}")
        os.remove("numbers.txt")
        os.remove("sorted.txt")

