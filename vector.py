from argparse import ArgumentError
from math import sqrt


class Vector:
    def __init__(self, values):
        self.__vec = values

    def __iter__(self):
        return iter(self.__vec)

    def __next__(self):
        for x in self.__vec:
            yield x
        raise StopIteration

    def __add__(self, other):
        if len(self) != len(other):
            raise ArgumentError
        return Vector([x + y for x, y in zip(self, other)])

    def __sub__(self, other):
        if len(self) != len(other):
            raise ArgumentError
        return Vector([x - y for x, y in zip(self, other)])

    def __mul__(self, other):
        if isinstance(other, Vector) and len(self) == len(other):
            return sum([x * y for x, y in zip(self, other)])
        return Vector([x * other for x in self])

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        return all([x == y for x, y in zip(self, other)])

    def __len__(self):
        return len(self.__vec)

    def norm(self):
        return sqrt(self * self)

    def get(self, i):
        if i < 0 or i > len(self):
            raise IndexError
        return self.__vec[i]

    def __str__(self):
        return "[" + ", ".join([f"{x}" for x in self.__vec]) + "]"
