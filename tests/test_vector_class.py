import unittest
import vector


class TestVector(unittest.TestCase):
    def setUp(self):
        self.vector_a = vector.Vector([1, 2, 3, 4, 5])
        self.vector_b = vector.Vector([6, 7, 8, 9, 10])
        self.vector_c = vector.Vector([11, 22, 33])

    def test_vector_len(self):
        expected = 5
        result = self.vector_a.len()
        self.assertTrue(expected == result)

    def test_vector_equals(self):
        self.assertTrue(vector.Vector([1, 2, 3, 4, 5]).equals(self.vector_a))
        self.assertFalse(self.vector_a.equals(self.vector_b))

    def test_vector_add(self):
        expected = vector.Vector([7, 9, 11, 13, 15])
        result = self.vector_a.add(self.vector_b)
        self.assertTrue(expected.equals(result))

    def test_vector_sub(self):
        expected = vector.Vector([-5, -5, -5, -5, -5])
        result = self.vector_a.sub(self.vector_b)
        self.assertTrue(expected.equals(result))

    def test_vector_mul(self):
        expected = vector.Vector([2, 4, 6, 8, 10])
        result = self.vector_a.mul(2)
        self.assertTrue(expected.equals(result))

    def test_vector_dot(self):
        expected = 130
        result = self.vector_a.dot(self.vector_b)
        self.assertTrue(expected == result)

    def test_vector_norm(self):
        self.assertTrue(vector.Vector([2, 2, 2, 2]).norm() == 4.)
