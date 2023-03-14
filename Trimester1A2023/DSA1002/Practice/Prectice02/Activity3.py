# def DecConvertor(x, target):
#     if target < 2 or target > 36:
#         raise ValueError("The base number has to be a integer and between 2 and 36")
#     if x < target - 1:
#         print()
#     if x >= (target - 1):
#         DecConvertor(x // target, target)
#     printer = x % target
#     if printer >= 10:
#         printer = chr(printer + 87)
#     print(printer, end = "")

def DecConvertor(x, base):
    if base < 2 or base > 36:
        raise ValueError("The base number has to be a integer and between 2 and 36")
    result = x % base
    if result >= 10:
        result = chr(result + 87)
    if x < 1:
        return str(x)
    else:
        return str(DecConvertor(x // base, base).lstrip("0")) + str(result)

if __name__ == "__main__":  
    for i in range(100):
        print(DecConvertor(i, 16))