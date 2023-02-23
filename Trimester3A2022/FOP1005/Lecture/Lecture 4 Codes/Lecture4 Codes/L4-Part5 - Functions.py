def print_lyrics():
	print("I'm a lumberjack, and I'm okay.")
	print("I sleep all night and I work all day.")


print_lyrics()

print()


def print_lyrics2(count):
	for i in range(count):
		print("I'm a lumberjack, and I'm okay.")
		print("I sleep all night and I work all day.")
	return("I'm okay")


print("Lumberjack Song")
result = print_lyrics2(3)
print(result)
