import os
import sys
import tempfile
import shutil


def split_file(name, chunk_size=5000):
    large_file = open(name)
    temp_list = []
    chunks = []
    size = 0

    try:
        os.mkdir("tmp")
    except FileExistsError:
        shutil.rmtree("tmp")
        os.mkdir("tmp")

    while True:
        number = large_file.readline()
        if not number:
            break
        temp_list.append(number)
        size += 1
        if size % chunk_size == 0:
            temp_list = sorted(temp_list, key=lambda num: int(num.strip()))
            chunk = tempfile.NamedTemporaryFile(dir=os.getcwd() + "/tmp",
                                                delete=False)
            chunk.writelines([string.encode("utf-8") for string in temp_list])
            chunk.seek(0)
            chunks.append(chunk)
            temp_list = []
    large_file.close()
    return chunks


def merge_sort(chunks, savefile_name="sorted.txt", chunk_size=5000):
    tree_list = []
    sorted_output = []
    savefile = open(savefile_name, "w")
    for chunk in chunks:
        tree_list.append((int(chunk.readline().strip()), chunk))

    mid = (len(tree_list) - 1) // 2
    while mid >= 0:
        heapify(tree_list, mid)
        mid -= 1

    current_size = 0
    while True:
        min = tree_list[0]
        if min[0] == sys.maxsize:
            break

        sorted_output.append(str(min[0]))
        current_size += 1
        if current_size > chunk_size:
            savefile.writelines(sorted_output)
            current_size = 0
            sorted_output = []
        chunk = min[1]
        number = chunk.readline().strip()

        if not number:
            number = sys.maxsize
        else:
            number = int(number)

        tree_list[0] = (number, chunk)
        heapify(tree_list, 0)

    for chunk in chunks:
        chunk.close()
    return savefile


def heapify(list, index):
    length = len(list)
    left = index * 2 + 1
    right = index * 2 + 2

    if left < length and list[left][0] < list[index][0]:
        smallest = left
    else:
        smallest = index

    if right < length and list[right][0] < list[smallest][0]:
        smallest = right

    if smallest != index:
        list[smallest], list[index] = list[index], list[smallest]
        heapify(list, smallest)


def main():
    chunks = split_file("numbers.txt", chunk_size=50000)
    file = merge_sort(chunks, chunk_size=50000)
    file.close()


if __name__ == "__main__":
    main()
