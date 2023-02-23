import numpy as np
import matplotlib.pyplot as plt

# fileobj = open("/home/tinigam/Desktop/FOP1005/PrecTest/PrecTest02/Data.csv")
# data = fileobj.readlines()
# fileobj.close()

# x_value = []
# y_value = []

# for line in data:
#     line = line.strip()
#     splitline = line.split(",")
#     x_value.append(int(splitline[0]))
#     y_value.append(int(splitline[1]))

# numarray = np.array([x_value, y_value])

# plt.subplot(1,2,1)
# plt.title
# plt.plot(x_value, y_value)

# plt.subplot(1,2,2)
# plt.title
# plt.bar(x_value,y_value)

# plt.show()

def file_reading(path):
    fileobj = open(path)
    data = fileobj.readlines()
    fileobj.close()

    x_value = []
    y_value = []

    for line in data:
        line = line.strip()
        splitline = line.split(",")
        x_value.append(int(splitline[0]))
        y_value.append(int(splitline[1]))

    numarray = np.array([x_value, y_value])
    return numarray

def plotting(x, y, title):
    plt.suptitle(title)
    plt.subplot(1,2,1)
    plt.title("Scatter")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.scatter(x, y)
    plt.subplot(1,2,2)
    plt.title("Bar")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.bar(x, y)

    plt.show()

path = "/home/tinigam/FOP1005/PrecTest/PrecTest02/Data.csv"
file_reading(path)
plotting(file_reading(path)[0], file_reading(path)[1], "Data")