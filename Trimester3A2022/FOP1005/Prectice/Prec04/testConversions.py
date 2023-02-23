#
# testConversions.py - tests the functions in conversions.py
#
from conversions import *
print("\nTESTING CONVERSIONS\n")
testF = 100
testC = fahr2cel(testF)
testK = fahr2kel(testF)
print("Fahrenheit is ", testF, " Celsius is ", testC, " Kelvin is ", testK)
print(fahr2cel.__doc__)
print(fahr2kel.__doc__)
print()

testC = 100
testF = cel2fahr(testC)
testK = cel2kel(testK)
print("Celsius is ", testC, "Fahrenheit is ", testF, " Kelvin is ", testK)
print(cel2fahr.__doc__)
print(cel2kel.__doc__)
print()

testK = 100
testF = kel2fahr(testK)
testC = kel2cel(testK)
print("Kelvin is ", testK, "Celsius is ", testC, "Fahrenheit is ", testF)
print(kel2cel.__doc__)
print(kel2fahr.__doc__)
