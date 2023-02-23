#
# textfun.py – module of text-related functions
#
vowels = 'aeiouAEIOU'

def novowels(inString):
	outString=''
	for i in inString:
		if not i in vowels:
			outString = outString + i
	return outString

def reverseupper(inString):
	return(inString[::-1].upper())