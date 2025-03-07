spots = [ 0,0,0,1,0,0,0,1,0,0,0,2,
          0,0,0,1,0,0,0,1,0,0,0,2,
          3,3,3,3,3,3,3,3,3,3,3,2,
          0,0,0,1,0,0,0,1,0,0,0,2,
	  3,3,3,3,3,3,3,3,3,3,3,2,
	  0,0,0,1,0,0,0,1,0,0,0,2,
	  0,0,0,1,0,0,0,1,0,0,0,2 ]
# Indexes for x's or o's: 13, 17, 21,
#			  37, 41, 45,
# 			  61, 65, 69
# Board
#   |   |   
#   |   |
#-----------
#   |   |
#-----------
#   |   |
#   |   |
#
def fillSpot(letter, quadrant):
	if letter == 'x':
		choice = 4
	else:
		choice = 5

	if quadrant == 1:
		spots[13] = choice
	elif quadrant == 2:
		spots[17] = choice
	elif quadrant == 3:
		spots[21] = choice
	elif quadrant == 4:
		spots[37] = choice
	elif quadrant == 5:
		spots[41] = choice
	elif quadrant == 6:
		spots[45] = choice
	elif quadrant == 7:
		spots[61] = choice
	elif quadrant == 8:
		spots[65] = choice
	else:
		spots[69] = choice
def printBoard():
	for s in spots:
		if s == 0:
			print(' ', end = '')
		elif s == 1:
			print('|', end = '')
		elif s == 2:
			print()
		elif s == 3:
			print('-', end = '')
		elif s == 4:
			print('x', end = '')
		elif s == 5:
			print('o', end = '')
		else:
			print("ERROR!")


printBoard()
for x in range(1,10):
	fillSpot('x', x)
	printBoard()