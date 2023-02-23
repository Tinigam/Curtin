#
#Student Name: Gao Yuyang
#Student ID: 21297919
#
#Practical Test 1, Q1
# P_test1.py: Creative string printing
Welcome = "Welcome to Curtin College"
Unit = "Fundamentals of Programming <202203A>"
print("\n\tPractical Test 1:\n")
Name = input('Enter your name:')
LastName =input('Enter last name:')
# Add print statement after this line; printing the “Welcome” and “Unit” strings as per the output.
print(Name)
print(LastName)
print(Welcome)
print(Unit)

#Add print statement to print names as per given format (see output)
print(LastName.upper(), " ", Name)

# Add for loop after this line to print the last part of the output.
Welcome = Welcome.upper()
for i in range(0,len(Welcome),2):
    print(Welcome[i], end='')