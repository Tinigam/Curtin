import random
base = 1
height = 1
r = 1/0.5
#Need to use similar triangle property to determine if in or out of tri

num_trials = 900000
in_tri = 0
for n in range(num_trials):
	x = random.random()
	y = random.random()

	if(x<0.5):
		if(y/x<r):
			in_tri+=1
	else:
		if(y/(x-0.5)<r):
			in_tri+=1
		
print(in_tri/num_trials*base*height)