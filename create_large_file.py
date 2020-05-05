#! /usr/bin/python3

import random


def create_file(filename, size):
    with open(filename, "w") as f:
        f.writelines("{}\n".format(random.randint(-1000000, 1000000)) for _ in range(size))


if __name__ == "__main__":
    create_file("numbers.txt", 5000000)
