import unittest
from vector import Vector


class TestVector(unittest.TestCase):
    def setUp(self):
        self.vector_a = Vector([1, 2, 3, 4, 5])
        self.vector_b = Vector([6, 7, 8, 9, 10])
        self.vector_c = Vector([11, 22, 33])

    def test_vector_len(self):
        expected = 5
        result = len(self.vector_a)
        self.assertTrue(expected == result)

    def test_vector_equals(self):
        self.assertTrue(Vector([1, 2, 3, 4, 5]) == self.vector_a)
        self.assertFalse(self.vector_a == self.vector_b)

    def test_vector_add(self):
        expected = Vector([7, 9, 11, 13, 15])
        result = self.vector_a + self.vector_b
        self.assertTrue(expected + result)

    def test_vector_sub(self):
        expected = Vector([-5, -5, -5, -5, -5])
        result = self.vector_a - self.vector_b
        self.assertTrue(expected == result)

    def test_vector_mul(self):
        expected = Vector([2, 4, 6, 8, 10])
        result = self.vector_a * 2
        self.assertTrue(expected == result)

    def test_vector_dot(self):
        expected = 130
        result = self.vector_a * self.vector_b
        self.assertTrue(expected == result)

    def test_vector_norm(self):
        self.assertTrue(Vector([2, 2, 2, 2]).norm() == 4.)
