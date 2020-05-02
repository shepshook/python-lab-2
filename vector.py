from math import sqrt


class Vector:
    def __init__(self, values):
        self.__vec = values

    def add(self, other):
        if self.len() != other.len():
            raise Exception("Vectors must match their sizes!")
        result = []
        for i in range(self.len()):
            result.append(self.__vec[i] + other.get(i))
        return Vector(result)

    def sub(self, other):
        if self.len() != other.len():
            raise Exception("Vectors must match their sizes!")
        result = []
        for i in range(0, self.len()):
            result.append(self.__vec[i] - other.get(i))
        return Vector(result)

    def mul(self, number):
        result = []
        for i in range(self.len()):
            result.append(self.__vec[i] * number)
        return Vector(result)

    def dot(self, other):
        if self.len() != other.len():
            raise Exception("Vectors must match their sizes!")
        res = 0
        for i in range(self.len()):
            res += self.__vec[i] * other.get(i)
        return res

    def equals(self, other):
        if self.len() != other.len():
            return False
        for i in range(0, self.len()):
            if self.get(i) != other.get(i):
                return False
        return True

    def len(self):
        return len(self.__vec)

    def norm(self):
        return sqrt(self.dot(self))

    def get(self, i):
        if i < 0 or i > self.len():
            raise IndexError
        return self.__vec[i]

    def to_string(self):
        separator = ", "
        return "[" + separator.join([f"{x} " for x in self.__vec]) + "]"
