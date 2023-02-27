#
# assorted.py - selecting random biscuits from a pack
#
import random
suits = ["Heart","Diamond","Club","Spade"]
deck = []


for suit in suits:
    #card 1 to 10
    for n in range(1,11):
        cardName = suit+" "+str(n)
        deck.append(cardName)
    deck.append(suit+" Jack");
    deck.append(suit+" Queen");
    deck.append(suit+" King");
            

#print all cards
print("Print all cards before shuffle")
for card in deck:
    print(card)
print("No of cards in deck:{0}".format(len(deck)))

#shuffle deck
for i in range(100000):
    index1 = random.randint(0,len(deck)-1)
    index2 = random.randint(0,len(deck)-1)
    #swap the two cards
    card1 = deck[index1]
    card2 = deck[index2]
    deck[index1] = card2
    deck[index2] = card1
        
#print all cards after shuffle
print("#"*10)
print("Print all cards after shuffle")
for card in deck:
    print(card)
print("No of cards in deck:{0}".format(len(deck)))

print("#"*10)
print("Pick 5 cards for hand1")
#pick 5 cards from front
hand1 = []
for i in range(5):
    hand1.append(deck[0])
    del deck[0]
    
#pick 5 cards from front
print("Pick 5 cards for hand2")
hand2 = []
for i in range(5):
    hand2.append(deck[0])
    del deck[0]
   
print(hand1)
print(hand2)
print("No of cards left in deck:{0}".format(len(deck)))
    

    
    
    
##biscuits.extend(['Monte Carlo']*7)
##biscuits.extend(['Shortbread Cream']*7)
##biscuits.extend(['Delta Cream']*6)
##biscuits.extend(['Orange Slice']*6)
##biscuits.extend(['Kingston']*5)
#biscuits = ["a","b"]

#print('\nASSORTED CREAMS\n')
#print('There are ', len(biscuits), ' biscuits in the pack.')
#print('\n', biscuits, '\n')

#more = input('\nWould you like a biscuit (Y/N)... ')
#while more != 'N':
    #choice = random.randint(0,len(biscuits)-1)
    #print('Your biscuit is : ', biscuits[choice])
    #del biscuits[choice]
    ##check if any more biscuits left
    #if(len(biscuits)==0):
        #print("No more biscuit left!")
        #more = "N"
    #else:
        #more = input('\nWould you like a biscuit (Y/N)...')

#print('\nThere are ', len(biscuits), ' biscuits left.')
#print('\n', biscuits, '\n')