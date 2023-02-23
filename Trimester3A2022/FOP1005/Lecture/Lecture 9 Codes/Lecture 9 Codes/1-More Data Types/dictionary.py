# Dictionary – The Meaning of Liff
liff = {'Duddo': 'The most deformed potato in any given collection of potatoes.',
        'Fring': 'The noise made by a lightbulb that has just shone its last.',
        'Tonypandy': ' The voice used by presenters on children\'s television programmes.'}

liff['Wawne'] = 'A badly supressed yawn.'
liff['Woking'] = 'Standing in the kitchen wondering what you came in here for.'

# print(liff)
# print(liff['Duddo'])
# print(liff['Fring'])
# print(liff.keys())

#del liff['Fring']
#print(liff.keys())

print()
pops = {'New South Wales': 7757843,
        'Victoria': 6100877,
        'Queensland': 4860448,
        'South Australia': 1710804,
        'Western Australia': 2623164,
        'Tasmania': 519783,
        'Northern Territory': 245657,
        'Australian Capital Territory': 398349}

# print(pops['Victoria'])
# for p in pops:
# 	print(p)
# print()
# for k in pops.keys():
# 	print(k, ' : ', pops[k])

#print()
#Dice toss with maps
import random
import matplotlib.pyplot as plt

dicecount = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for i in range(1000):
	toss = random.randint(1, 6)
	dicecount[toss] += 1

plt.bar(dicecount.keys(), dicecount.values())
plt.show()

