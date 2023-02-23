#
# strings2.py: Read in a string and print it in forward using a loop and a method call
#

instring = input('Enter a string... ')
# *** add upper and duplicating code here
instring = instring.upper()* 2

# forwarding with a while loop

print('Forward string is : ', end='')
index = 1
while index <= len(instring) - 2:
    print(instring[index], end='')
    index = index + 2
print()

# forwarding with a range loop

print('Forward string is : ', end='')
for index in range(1, len(instring) -1, 2):
    print(instring[index], end='')
print()

# forwarding with slicing

print('Forward string is :', instring[1:-1:2])