import numpy as np

##list opertaion
#list1 = [1, 2, 3]
#list2 = [4, 5, 6]
#list3 = list1 + list2 #not addition!
#print(list3)
##list3 = list1 - list2 #error!
##cannot do math op on two lists, need numpy array to do that

#print()
#a = np.array([1, 2, 3])
#b = np.array([4, 5, 6])
#c = a + b #add each corresponding element
#print(c)
#c = a + 1 #add each element by 1
#print(c)
#c = a - b #substract each corresponding element
#print(c)
#c = a * b #multiply each corresponding element
#print(c)
#c = a / b #divide each corresponding element
#print(c)
##note for + - * /, the size of the two array must be the same

#print()
##Comparsions
#a = np.array([1, 2, 3])
#b = np.array([4, 5, 6])
#c = np.array([6, 5, 4])
#d = a < b #compare each corresponding element, result is an array of boolean
#print(d)
#d = a < 2 #compare each element with 2, result is an array of boolean
#print(d)
#d = b == c #compare each corresponding element, result is an array of boolean
#print(d)
#d = b <= c #compare each corresponding element, result is an array of boolean
#print(d)

##Element-wise Functions
#a = np.array([1, 2, 3])
#b = np.array([4, 5, 6])
#c = np.sqrt(a) #perform sqrt() function on each element
#print(c)
#c = np.sin(a) #perform sin() function on each element
#print(c)
##Also... exp(), cos(), log(), add(), multiply() etc.

##Array-wise Functions
#a = np.array([1, 2, 3])
#b = np.array([4, 5, 6])
#r = a.sum()
#print(r)
#r = b.min()
#print(r)
#r = b.max()
#print(r)
#r = a.mean()
#print(r)

##exchange rate example
#usdprices = np.array([10, 20, 30, 40, 50])
#exchrate = 1.3
#audprices = usdprices * 1.3
#print(audprices)

##Adding GST example
#prices = np.array([10, 20, 30, 40, 50])
#gstprices = prices * 1.1
#print(gstprices)

##Conversion miles to km
#distmiles = np.array([100, 150, 200, 250])
#mileskm = 1.60934
#distkm = distmiles * mileskm
#print(distkm)

##Temperatures example
#march2017 = np.array([37.7, 29.9, 35.2, 36.1, 36.2, 34.7, 33.8, 34.5, 31.9, 29.9, 30.9, 24.8, 24.2, 24.1, 24.0])
#print(march2017.min())
#print(march2017.max())
