numbers = [x for x in range(1, 6)]
print(numbers)

def triple(x):
    return x * 3
numbers = [triple(n) for n in numbers]
print(numbers)

stringToRead = "a1b2c3d4"
numbers = []
# for letter in stringToRead:
#     if letter.isdigit():
#         numbers.append(int(letter))
# print(numbers)

numbers = [int(x) for x in stringToRead if x.isdigit()]
print(numbers)

listOfWords = ["peter", "mary", "john"]

# for i in range(len(listOfWords)):
#     firstLetter = listOfWords[i][0].upper()
#     others = listOfWords[i][1:]
#     listOfWords[i] = firstLetter + others
# print(listOfWords)

listOfWords = [word[0].upper() + word[1:] for word in listOfWords]
print(listOfWords)