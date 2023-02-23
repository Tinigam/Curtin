#
# textfun.py – module of text-related functions
#
vowels = 'aeiouAEIOU'


def novowels(inString):
	outString = ''
	for i in inString:
		if not i in vowels:
			outString = outString + i
	return outString


def reverseupper(inString):
	return(inString[::-1].upper())


def main():
	print('\nTesting textfun.py')
	testString = 'helloHELLO'
	print('\nTest string is: ', testString)
	print('novowels: ', novowels(testString))
	print('reverseupper: ', reverseupper(testString))
	print('Testing complete')


#if we run textfun.py directly, main() will be called
if __name__ == '__main__':
	main()
