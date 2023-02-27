import random

#            0 1 2 3 4 5 
dice_count =[0,0,0,0,0,0]

trial_num = 10

for i in range(trial_num):
    dice_num = random.randint(1,6)
    dice_count[dice_num-1]+=1

for num in range(1,len(dice_count)+1):
    print("num:{0} count:{1}".format(num,dice_count[num-1]))