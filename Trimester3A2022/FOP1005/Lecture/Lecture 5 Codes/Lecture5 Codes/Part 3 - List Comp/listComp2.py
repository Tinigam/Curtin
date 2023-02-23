numbers = [1, 2, 3, 4, 5]
doubled_odds = []
for n in numbers:
	if n % 2 == 1:
		doubled_odds.append(n * 2)
		
print(doubled_odds)
print()

doubled_odds = [n * 2 for n in numbers if n % 2 == 1]
print(doubled_odds)