import unittest
import os
import time
import create_large_file
import external_sort


class TestExternalSortResult(unittest.TestCase):
    def setUp(self):
        self.input = os.getcwd() + "/numbers.txt"
        self.output = os.getcwd() + "/output.txt"
        create_large_file.create_file(self.input, 1000)

    def test_external_sort_result(self):
        external_sort.sort(self.input, self.output, 50)
        self.assertTrue(self.file_sorted())

    def file_sorted(self):
        with open(self.output, 'r') as file:
            a = file.readline()
            b = file.readline()
            while True:
                if b:
                    if int(a) > int(b):
                        return False
                    a = b
                    b = int(file.readline())
                else:
                    break
            return True

    def tearDown(self):
        os.remove(self.input)
        os.remove(self.output)


class TestExternalSortPerformance(unittest.TestCase):
    def setUp(self):
        self.input = os.getcwd() + "/numbers.txt"
        self.output = os.getcwd() + "/output.txt"
        create_large_file.create_file(self.input, 1000000)
        self.start_time = time.time()

    def test_external_sort_performance(self):
        external_sort.sort(self.input, self.output, 50000)

    def tearDown(self):
        print(f"Sorted 1000000 nums in {time.time() - self.start_time}")
        os.remove(self.input)
        os.remove(self.output)

