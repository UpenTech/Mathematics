import random as R

dice_MatrixA = []
dice_MatrixB = []

points = 0      				 #Storation  of Points

for i in range(4):           			 #2D List
	dice_MatrixA = []
	for j in range(4):
		dice_MatrixA.append(R.randrange(1,7))		#Rolling of dice
	dice_MatrixB.append(dice_MatrixA)			#Appending 2D List

test = 0

for i in range(4):
	print(dice_MatrixB[i])


for i in range(4):

	for j in range(4):
		if dice_MatrixB[i][j] % 2  != 0:	#Testing if Row is Even
			test = 1
			break


	if test == 0:
		points += 20

	test = 0

	for j in range(4):
		if dice_MatrixB[i][j] % 2 == 0:		#Testing if Row is Odd
			test = 1
			break

	if test == 0:
		points += 20

	test = 0

for i in range(4):

	for j in range(4):
		if dice_MatrixB[j][i] % 2 == 0:		#Testing if Column is Odd
			test = 1
			break

	if test == 0:
		points += 20

	test = 0

	for j in range(4):
		if dice_MatrixB[j][i] % 2 != 0:		#Testing if Column is Even
			test = 1
			break

	if test == 0:
		points += 20

	test = 0


for i in range(0,4,3):				#Testing if 4-Corners are Odd
	for j in range(0,4,3):
		if dice_MatrixB[i][j] % 2 == 0:
			test = 1
			break

if test == 0:
	points += 20

test = 0

for i in range(0,4,3):				#Testing if 4-Corners are Even
	for j in range(0,4,3):
		if dice_MatrixB[i][j] % 2 != 0:
			test = 1
			break

if test == 0:
	points += 20

test = 0


for i in range(4):
	if dice_MatrixB[i][i] % 2  ==  0:		#Testing Diagonal are Odd
		test = 1
		break

if test == 0:
	points += 20

test = 0

for i in range(4):
	if dice_MatrixB[3-i][i] % 2  ==  0:            #Testing Diagonal are Odd
		test = 1
		break

if test == 0:
	points += 20

test = 0

for i in range(4):
	if dice_MatrixB[i][i] % 2  !=  0:		#Testing Diagonal are Even
		test = 1
		break

if test == 0:
	points += 20

test = 0

for i in range(4):
	if dice_MatrixB[3-i][i] % 2  !=  0:            #Testing Diagonal are Even
		test = 1
		break

if test == 0:
	points += 20

test = 0

print("Points: " + str(points))
