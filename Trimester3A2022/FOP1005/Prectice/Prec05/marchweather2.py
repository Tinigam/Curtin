import matplotlib.pyplot as plt

fileobj = open('/home/tinigam/Desktop/FOP1005/Prectice/Prec05/marchweatherfull.csv', 'r')
data = fileobj.readlines()
fileobj.close()

mins = [] # do the same for maxs, nines and threes
maxs = []
nines = []
threes = []

for line in data:
    splitline = line.split(',')
    mins.append(float(splitline[1]))
    maxs.append(float(splitline[2]))
    nines.append(float(splitline[9]))
    threes.append(float(splitline[15]))

dates = range(1,32)

plt.plot(dates, mins, dates, maxs, dates, nines, dates, threes)
plt.show()

file2 = open('/home/tinigam/Desktop/FOP1005/Prectice/Prec05/marchout.csv', 'w')
for i in range(len(mins)):
    file2.write(str(mins[i]) + ',' + str(maxs[i]) + ',' + str(nines[i]) + ',' + str(threes[i]) + '\n')
file2.close()