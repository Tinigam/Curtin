with open('names.txt', 'r') as f:
	read_data = f.read()
	print(read_data)
print()
with open('names.txt', 'r') as f:
	for line in f:
		print(line,end="")