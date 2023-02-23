# 
# strings1.py: Read in a string and print it in reverse 
# 
# instring = input('Enter a string... ') 
# Example: reversing with a for-range loop 
# 
#print('String is : ', end='') 
#for index in range(len(instring)-1,-1,-1): 
# print(instring[index], end='') 
# 
# Example: reversing with slicing 
# 
#print('String is :', instring[::-1]) 

# Convert instring to lowercase and print it

instring = "A Moose Once Bit My Sister"
instringlower = instring.lower()
print(instring, ' would become:', instringlower)

# Print the string going backwards with for-range, ending at the fifth letter and printing every third letter
print(instring, ' would become: ', end='')
for i in range(len(instring)-1, 4, -1):
    if (i+1) % 3 == 0:
        print(instring[i], end="")
print()

# Print the string going forwards with slicing, starting at the second letter, ending at the second-last letter and printing every third letter
print(instring, ' would become: ',instring[1:-1:3])
print()