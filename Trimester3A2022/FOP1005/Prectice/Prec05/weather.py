#
# weather.py: Print min and max temps from a file
# (source: http://www.bom.gov.au/climate/)

import matplotlib.pyplot as plt

path = '/home/tinigam/Desktop/FOP1005/Prectice/Prec05/marchweather.csv'
fileobj = open(path, 'r')

# add file reading code here

mins = fileobj.readline()
maxs = fileobj.readline()

fileobj.close()

mins = [float(temp) for temp in mins.split(",")]
maxs = [float(temp) for temp in maxs.split(",")]
print(mins)
print(maxs)

dates = range(1,32)

plt.plot(dates, mins, dates, maxs)
plt.show()