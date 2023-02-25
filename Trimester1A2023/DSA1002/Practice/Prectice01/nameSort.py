from SortFilesPython import DSAsorts
import sys

path = "/home/Tinigam/Curtin/Trimester1A2023/DSA1002/Practice/Prectice01/RandomNames7000.csv"
sort = "b"

if len(sys.argv) > 1:
    sort = sys.argv[1]

with open(path) as data_file:
    data = data_file.readlines()
    if sort == "b":
        DSAsorts.bubbleSort(data)
    elif sort == "i":
        DSAsorts.insertionSort(data)
    elif sort == "s":
        DSAsorts.selectionSort(data)
    else:
        print("Unsupported array type")
    for line in data:
        print(line, end = "")