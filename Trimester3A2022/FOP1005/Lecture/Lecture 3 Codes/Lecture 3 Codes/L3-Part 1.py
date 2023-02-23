import numpy as np

#myarray = np.array([1, 2, 3])
#print(myarray)

#array1 = np.array([1, 2, 3, 4, 5])
#print(array1)

##all numbers are float in the array
#templist = [1.0, 2.0, 3.0, 4.0]
#array2 = np.array(templist)
#print(array2)

##all numbers are int in the array
#templist2 = [1, 2, 3, 4, 5]
##convert all int to float using dtype (data type)
#array2 = np.array(templist2, dtype=float)
#print(array2) #note of "." behind each int

##use index to access the item in the array
#print("array1: ", array1)
#print('Element zero is: ', array1[0])
#array1[2] = 5 #change item in index 2 to 5
#print(array1)
##access item in index 1 and 2 and add them up
#sumoftwo = array1[1] + array1[2]
#print(sumoftwo)

##Access parts of the array with slicing:
#array1 = np.array([1, 2, 3, 4, 5])
#print(array1)
#print(array1[1:3]) #note slice from index 1 to 3-1 (i.e. 1 to 2)

##Preset arrays
##Create an array of 100 float (default), all set to 0
#zeroarray = np.zeros(100)
#print(zeroarray)
##Create an array of 100 integers, all set to 1
#onesarray = np.ones(100, dtype=int)
#print(onesarray)
##Create an array of 100 floats, all set to 1
#onesarray = np.ones(100)
#print(onesarray)
##Array of 50 floats, each set to 100
##Code is not working in slides!
#hundreds = np.empty(100) #create an array of size 100
#hundreds.fill(50) #change all the values to 50
#print(hundreds)
##Array of 50 random numbers
#randarray = np.random.random(50)
#print(randarray)


##Revision on range with list
#print(list(range(10))) #list of 0 to 9
#print(list(range(5, 16))) #list of 5 to 16-1
#print(list(range(5, 16, 2))) #list of 5 to 16-1 with a step 2
#print(list(range(5, 0, -1))) #list of 5 to 0+1 with step of -1

##Arrays with ranges of numbers
##arange => array range (note: not arrange!)
##same concept as range in list
#fives = np.arange(0, 55, 5) #array of 0 to 54 with step of 5
#print(fives)

#tens = np.arange(0, 55, 10) #array of 0 to 54 with step of 10
#print(tens)

##linespace indicate how many values inbetween
#tofifty = np.linspace(0, 50, 5) #0 to 50 with 5 numbers inbetween
#print(tofifty)

#toten = np.linspace(0, 10, 10) # to to 10 with 10 numbers inbetween
#print(toten)

##while loop with array
#tofifty = np.linspace(0, 50, 5)
#print(tofifty)
#index = 0
#while index < len(tofifty):
	#print('Element ', index, ' is: ', tofifty[index])
	#index = index + 1

#print()
##for loop with array
#for index in range(0, len(tofifty)):
	#print('Element ', index, ' is: ', tofifty[index])

#print()
#for item in tofifty:
	#print('Element is: ', item)

##revision: slicing string
#s = "123456789"
##    012345678 <= index of each char
#print(s[1:3]) #slice from index 1 to 3-1
#print(s[:3]) #slice from index 0 to 3-1
#print(s[3:]) #slice from index 3 to the end
#print(s[3:7:2]) #slice from index 3 to 7-1 with a step of 2
##think of what range(3:7:2) gives ? => [3,5] , that extract out each char using the generate index
#print(s[::2]) #slice from index 0 to the end with a step of 2

##backwards => use negative step
#print()
#print(s[::-1]) #from last index to index 0 with step of -1
#print(s[::-2]) #from last index to index 0 with step of -2
#print(s[7:2:-2]) #from index 7 to index 2+1 with step of -2
##think of range(7, 2, -2) => [7,5,3], use the generate index to extract
#print(list(range(7, 2, -2))) #=>[7,5,3]

#print()
##slicing array -> similar to slicing string
#myarray = np.arange(1, 10)
#print(myarray)
#print(myarray[1:3]) #will give elements index 1 and 3-1
#print(myarray[:3]) # will give elements index 0 to 3-1
#print(myarray[3:]) # will give elements index 3 to the end
#print(myarray[3::2]) #will give elements index 3 to the end with  step of 2
#print(myarray[::2]) # will give elements index 0 to the end with step of 2

##Slicing to make new arrays
#tofifty = np.linspace(0, 50, 5)
#print(tofifty)
#tofifty2 = tofifty[1:3]
#print(tofifty2)
#tofifty3 = tofifty[::2]
#print(tofifty3)
