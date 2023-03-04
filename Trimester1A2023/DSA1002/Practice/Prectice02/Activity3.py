def DecConvertor(x, target):
    if x >= (target - 1):
        DecConvertor(x // target, target)
    print(x % target, end = "")

DecConvertor(100, 2)
print()