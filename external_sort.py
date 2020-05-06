import os
import sys
import tempfile
from shutil import rmtree
from linecache import getline


def sort(filename, sorted_name, chunk_size):
    chunks = split_file(filename, chunk_size=chunk_size)
    file = merge_sort(chunks, chunk_size=chunk_size, savefile_name=sorted_name)
    file.close()


def split_file(name, chunk_size=5000):
    large_file = open(name)
    temp_list = []
    chunks = []
    size = 0

    try:
        os.mkdir("tmp")
    except FileExistsError:
        rmtree("tmp")
        os.mkdir("tmp")

    while True:
        number = large_file.readline()
        if not number:
            break
        temp_list.append(number)
        size += 1
        if size % chunk_size == 0:
            temp_list = sorted(temp_list, key=lambda num: int(num.strip()))
            chunk = tempfile.NamedTemporaryFile(dir=os.getcwd() + "/tmp", delete=False)
            # dump all collected numbers into new temp file
            chunk.writelines([string.encode("utf-8") for string in temp_list])
            chunk.close()
            # save only the name of the file
            chunks.append(chunk.name)
            temp_list = []
    large_file.close()
    return chunks


def merge_sort(chunks, savefile_name="sorted.txt", chunk_size=5000):
    tree_list = []
    sorted_output = []
    current_chunk_line = {}
    savefile = open(savefile_name, "w")
    for chunk in chunks:
        with open(chunk, "r") as file:
            tree_list.append((int(file.readline().strip()), chunk))
        current_chunk_line[chunk] = 1

    mid = (len(tree_list) - 1) // 2
    while mid >= 0:
        heapify(tree_list, mid)
        mid -= 1

    current_size = 0
    while True:
        min_ = tree_list[0]
        if min_[0] == sys.maxsize:
            break

        sorted_output.append(str(min_[0]))
        current_size += 1
        if current_size > chunk_size:
            savefile.writelines(sorted_output)
            current_size = 0
            sorted_output = []
        chunk_name = min_[1]
        number = getline(chunk_name, current_chunk_line[chunk_name]).strip()
        current_chunk_line[chunk_name] += 1

        if not number:
            number = sys.maxsize
        else:
            number = int(number)

        tree_list[0] = (number, chunk_name)
        heapify(tree_list, 0)

    for chunk_name in chunks:
        os.remove(chunk_name)

    return savefile


def heapify(list_, index):
    length = len(list_)
    left = index * 2 + 1
    right = index * 2 + 2

    if left < length and list_[left][0] < list_[index][0]:
        smallest = left
    else:
        smallest = index

    if right < length and list_[right][0] < list_[smallest][0]:
        smallest = right

    if smallest != index:
        list_[smallest], list_[index] = list_[index], list_[smallest]
        heapify(list_, smallest)


def main():
    chunks = split_file("numbers.txt", chunk_size=50000)
    file = merge_sort(chunks, chunk_size=50000)
    file.close()


if __name__ == "__main__":
    main()
