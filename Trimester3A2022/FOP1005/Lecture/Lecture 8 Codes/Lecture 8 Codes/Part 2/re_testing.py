import re

p = re.compile(r'[test]')
##as long as the re matching letter has one of the character inside
strings_to_test = ["test", "est", "st", "tea", "abc", "es", "aes"]

# p = re.compile(r'[cbm]at')
# #the first re letter must be c,b or m followed by "at"
# strings_to_test = ["cat","bat","mat","caa","dat","xcat","ca","ct"]

#p = re.compile(r'[^5]')
##first re letter must not be 5
#strings_to_test = ["512","215"]

#compare [] and ()
#the first two re letters must match "15"
# p = re.compile(r'(15)')
# ##first re letter must be 5
# strings_to_test = ["512","215","111"]

# #as long as the first re letter has a 1 or 5
# p = re.compile(r'[15]')
# ##first re letter must be 5
# strings_to_test = ["512","215","111"]


# p = re.compile(r'[\d]')
# #first re letter must be a digit
# strings_to_test = ["512","apple","111","apple1"]


# p = re.compile(r'[\D]')
# #first re letter must not be a digit
# strings_to_test = ["512","apple","111","apple1","1apple"]

#p = re.compile(r'.at')
##matches anything with a character followedby "at"
#strings_to_test = ["bat","apple"," at","baat"]

#p = re.compile(r'[0-9][a-z]')
## matches any digit followed by a lower case character
#strings_to_test = ["1a","2b","c3"," 1a"," 2b"]


#p = re.compile(r'[0-9]\s[a-z]')
##– matches any digit followed by a
##whitespace charcater, followed by a lower case character
#strings_to_test = ["1a","2 b","3 3","ddd 4 dddd"]

##ca*t matches to ct, cat, caaat, caaaaaat
#p = re.compile(r'ca*t')
##– matches any digit followed by a
##whitespace charcater, followed by a lower case character
#strings_to_test = ["ct","cat","caat","caaaaat","xct","xcat"]


##ca+t matches to cat, caaat, caaaaaat but not ct
#p = re.compile(r'ca+t')
##– matches any digit followed by a
##whitespace charcater, followed by a lower case character
#strings_to_test = ["ct","cat","caat","caaaaat","xct","xcat"]

##{m,n} matches at least m repeats and at most n repeats
#p = re.compile(r'ab{1,3}c')
#strings_to_test = ["ac","abc","abbc","abbbc","abbbbc","xxacxx","xxabcxx","xxabbcxx","xxabbbcxx","xxabbbbcxx"]

#match to beginning of string
print("match to beginning of string")
for s in strings_to_test:
	r = p.match(s)
	if(r):
		print(s)
print()
print("search - match to anywhere in the string")
for s in strings_to_test:
	r = p.search(s)
	if(r):
		print(s)
