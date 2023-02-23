import re

phoneRegex = re.compile(r'''(
(\d{2}|\(\d{2}\))  #first two letter is digit or first letter is "(" followed by two digits and followed by ")"  
(\s|\.)?           #\s – matches any whitespace character or \.matches anything other than newline
(\d{4}\s\d{4})     #matches any 4 digits followed by \s followed by any 4 digits
)''', re.VERBOSE)

fileobj = open('/home/tinigam/FOP1005/Lecture/Lecture 8 Codes/Lecture 8 Codes/Part 2/phone.txt')
data = fileobj.readlines()

for number in data:
	number = number.strip()
	mo = phoneRegex.search(number)
	if mo:
		print(number + ' found ' + mo.group())