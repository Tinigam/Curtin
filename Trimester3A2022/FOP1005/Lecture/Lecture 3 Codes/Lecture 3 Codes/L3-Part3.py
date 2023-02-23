import matplotlib.pyplot as plt
import numpy as np

##Line Plot
#plt.plot([1, 2, 3, 4])
#plt.ylabel('Some Numbers')
#plt.show()

##March Temperature
#march2017 = np.array([37.7, 29.9, 35.2,
                      #36.1, 36.2, 34.7, 33.8, 34.5, 31.9, 29.9,
                      #30.9, 24.8, 24.2, 24.1, 24.0])
#dates = range(1, len(march2017) + 1)
#plt.plot(dates, march2017)
#plt.title('March Temperatures')
#plt.ylabel('Temperature')
#plt.xlabel('Date')
#plt.show()

##March Temperatures – red dots
#march2017 = np.array([37.7, 29.9, 35.2,
                      #36.1, 36.2, 34.7, 33.8, 34.5, 31.9, 29.9,
                      #30.9, 24.8, 24.2, 24.1, 24.0])
#dates = range(1, len(march2017) + 1)
#plt.plot(dates, march2017, "ro") #r-red o-dot
#plt.title('March Temperatures')
#plt.ylabel('Temperature')
#plt.xlabel('Date')
#plt.show()

##Multiple plots on an axis
##evenly sampled time at 200ms intervals
#t = np.arange(0., 5., 0.2)
#t2 = t**2
#t3 = t**3
## red dashes, blue squares and green triangles
#plt.title('Multiline')
#plt.plot(t, t, 'r--', t, t2, 'bs', t, t3, 'g^')
## "r--" => red dashes
## "bs" => blue squares
## "g^" => green triangles
#plt.show()

#Subplots 2 by 1
#march2017 = np.array([37.7, 29.9, 35.2, 36.1, 36.2, 34.7, 33.8, 34.5, 31.9, 29.9, 30.9, 24.8, 24.2, 24.1, 24.0])
#dates = range(1, len(march2017) + 1)
#plt.figure(1)
#plt.subplot(211) #2 rows, 1 col, subplot 1
#plt.plot(dates, march2017, '--')
#plt.title('March Temperatures')
#plt.ylabel('Temperature')

#plt.subplot(212) #2 row, 1 col, subplot 2
#plt.plot(dates, march20s17, 'ro')
#plt.ylabel('Temperature')
#plt.xlabel('Date')
#plt.show()

##Subplots 2 by 2
#march2017 = np.array([37.7, 29.9, 35.2, 36.1, 36.2, 34.7, 33.8, 34.5, 31.9, 29.9, 30.9, 24.8, 24.2, 24.1, 24.0])
#dates = range(1, len(march2017) + 1)

#plt.figure(1)
#plt.subplot(221)
#plt.plot(dates, march2017, '--')
#plt.title('March Temperatures')
#plt.ylabel('Temperature')
#plt.subplot(222)
#plt.plot(dates, march2017, 'ro')
#plt.ylabel('Temperature')
#plt.xlabel('Date')
#plt.subplot(223)
#plt.plot(dates, march2017, 'g^')
#plt.ylabel('Temperature')
#plt.xlabel('Date')
#plt.subplot(224)
#plt.plot(dates, march2017, 'bs')
#plt.ylabel('Temperature')
#plt.xlabel('Date')

#plt.show()


##bar chart example
#x_values = [1, 2, 3, 4, 5, 6]
#y_values = [4, 7, 5, 3, 2, 1]
#width = 0.9
#plt.bar(x_values, y_values, width, color='purple')
#plt.show()

##Roll the Dice example using bar chart
##we trhow the dice for trials number of times
##record down how many 1,2,3,4,5,6, then plot the bar chart
#import random
#dice = ['one', 'two', 'three', 'four', 'five', 'six']
#one, two, three, four, five, six = 0, 0, 0, 0, 0, 0
#trials = 1000
#print('\nDICE TOSS\n')
#for index in range(trials):
   #choice = random.choice(dice)
   #if choice == 'one':
      #one += 1
   #elif choice == 'two':
      #two += 1
   #elif choice == 'three':
      #three += 1
   #elif choice == 'four':
      #four += 1
   #elif choice == 'five':
      #five += 1
   #else:
      #six += 1

#print('\nRESULTS\n')
#print('1: ', one)
#print('2: ', two)
#print('3: ', three)
#print('4: ', four)
#print('5: ', five)
#print('6: ', six)

#plt.title('Roll the Dice')
#plt.xlabel('Number')
#plt.ylabel('Count')
#plt.bar([1, 2, 3, 4, 5, 6], [one, two, three, four,
        #five, six], 0.9, color='purple')
#plt.show()

#histograms
#https://www.mathsisfun.com/data/histograms.html
#to genrate a histograms, we need a large amount of data

#generate random 1000 data from normal distribition
#https://www.mathsisfun.com/data/standard-normal-distribution.html
from numpy.random import normal
gaussian_numbers = normal(size=1000)
plt.hist(gaussian_numbers)
#comment and uncomment the following plt.hist() to test out

#note normed is deprecate, use density
#plt.hist(gaussian_numbers, bins=20, density=True) # note the range of the y axis

#plt.hist(gaussian_numbers, bins=20, cumulative=True)

#plt.hist(gaussian_numbers, histtype='step', alpha=0.5)

#plt.hist(gaussian_numbers, bins=20, density=True, cumulative=True, color=['purple'])

plt.title("Gaussian Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

