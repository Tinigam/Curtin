# names = open('/home/tinigam/Desktop/FOP1005/Lecture/Lecture5 Codes/Lecture5 Codes/Part 1 - Files/names.txt')
# thischunk = names.read()
# print(thischunk)
# names.close()

# names = open('/home/tinigam/Desktop/FOP1005/Lecture/Lecture5 Codes/Lecture5 Codes/Part 1 - Files/names.txt')
# thischunk = names.readline()
# print(thischunk)
# thischunk = names.readline()
# print(thischunk)
# names.close()

names = open('/home/tinigam/Desktop/FOP1005/Lecture/Lecture5 Codes/Lecture5 Codes/Part 1 - Files/names.txt')
thischunk = names.readlines()
print(thischunk)
names.close()

for name in thischunk:
    print(name.strip())
names.close()
