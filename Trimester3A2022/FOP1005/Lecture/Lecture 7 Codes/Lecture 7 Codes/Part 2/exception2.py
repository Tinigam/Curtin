#with checks
n = None
while n is None:
	s = input("Enter an integer: ")
	if s.lstrip('-').isdigit():
		n = int(s)
	else:
		print("%s is not an integer." % s)
		
# with exception handling
n = None
while n is None:
	try:
		s = input("Enter an integer: ")
		n = int(s)
	except ValueError:
		print("%s is not an integer." % s)