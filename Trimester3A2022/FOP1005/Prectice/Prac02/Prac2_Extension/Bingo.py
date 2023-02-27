import random
bingo = []

#construct bingo
for row_index in range(18):
	#construct one row
	each_row = []
	for col_index in range(9):
		each_row.append("")
	bingo.append(each_row)

for col_index in range(9):
	#generate the number to be inserted into bingo
	if(col_index==0):
		startNum = 1
		endNum = 10
	else:
		startNum = 10*col_index
		endNum = 10+10*col_index
	num_range = list(range(startNum,endNum))
	
	while (len(num_range)>0):
		#get a random row index to insert
		row_index_to_index = random.randint(0,17)
		#check if that slot is occupied
		#if not occupied, insert a random num in num_range into bingo
		if(bingo[row_index_to_index][col_index]==""):
			#pick a num in num_range
			r_index = random.randint(0,len(num_range)-1)
			bingo[row_index_to_index][col_index] = num_range[r_index]
			del num_range[r_index]
		#if occupied skip and look for another slot
		
		
for row in bingo:
	print(row)