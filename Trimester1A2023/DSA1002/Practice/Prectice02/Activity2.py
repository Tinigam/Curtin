def gcd(x, y):
    while y:
        x, y = y , x % y
    return x

def recursiveGcd(x, y):
    if y == 0:
        return abs(x)
    else:
        return recursiveGcd(y, x % y)
