import sys
punctuation = '~!@#$%^&*()_+{}|:"<>?`=[]\\;\',./'
if len(sys.argv) < 2:
	filename = '/home/tinigam/FOP1005/Lecture/Lecture 9 Codes/Lecture 9 Codes/1-More Data Types/grimm.txt'
else:
	filename = sys.argv[1]

book = open(filename).read()
bookP = book.translate(str.maketrans('', '', punctuation))
words = bookP.lower().split()
print(len(words))
print(words[:10])

wordfreq = {} # empty dictionary
for word in words: # for each word
	if word not in wordfreq: # if it's not in dict
		wordfreq[word] = 0
	wordfreq[word] += 1

print(len(wordfreq))
print(wordfreq)
