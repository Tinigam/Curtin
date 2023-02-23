divisible_by_7 = [x for x in range(50,151) if x % 7 == 0]
multiples_of_31 = [x * 31 for x in range(3, 22, 3)]
divisible_by_4_and_7 = [x for x in range(31, 10, -1) if x % 4 == 0 and x % 7 == 0]
wordlist = ["Apple", "kite", "Kangaroo", "Pumpkin"]
words_starting_with_k = [x for x in wordlist if x[0] == "K" or x[0] == "k"]
print(divisible_by_7)
print(multiples_of_31)
print(divisible_by_4_and_7)
print(words_starting_with_k)