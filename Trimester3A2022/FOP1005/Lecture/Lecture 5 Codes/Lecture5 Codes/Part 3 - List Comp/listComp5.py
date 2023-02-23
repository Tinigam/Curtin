list1 = [3,4,5]
multiplied = [item*3 for item in list1]
print(multiplied)

def double(x):
	return x*2
doubled = [double(x) for x in range(10)]
print(doubled)