# create heat source
hlist = []
fileobj = open('/home/tinigam/Desktop/FOP1005/Lecture/Lecture5 Codes/Lecture5 Codes/Part 3 - List Comp/heatsource.csv','r')
for line in fileobj:
	line_s = line.strip()
	ints = [int(x) for x in line_s.split(',')]
	hlist.append(ints)
fileobj.close()

print(hlist)

for i in hlist:
	print(i)