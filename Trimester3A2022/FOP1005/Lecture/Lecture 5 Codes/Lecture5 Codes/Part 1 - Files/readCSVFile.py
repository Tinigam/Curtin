namesfile = open('/home/tinigam/Desktop/FOP1005/Lecture/Lecture5 Codes/Lecture5 Codes/Part 1 - Files/names.csv')
line = namesfile.readline()
print(line)
linelist = line.split(',')
print(linelist)
for name in linelist:
    print(name)

print()
path = "/home/tinigam/Desktop/FOP1005/Lecture/Lecture5 Codes/Lecture5 Codes/Part 1 - Files/names3.csv"
newnames = open(path, 'w')
newline = ','.join(linelist)
print(newline)
newnames.write(newline)
