spots = [ 0,0,0,1,0,0,0,1,0,0,0,2,
          0,0,0,1,0,0,0,1,0,0,0,2,
          3,3,3,3,3,3,3,3,3,3,3,2,
          0,0,0,1,0,0,0,1,0,0,0,2,
	  3,3,3,3,3,3,3,3,3,3,3,2,
	  0,0,0,1,0,0,0,1,0,0,0,2,
	  0,0,0,1,0,0,0,1,0,0,0,2 ]

player_spots = [ 0,0,0,
		 0,0,0,
		 0,0,0 ]
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
		player_spots[quadrant-1] = 1
	else:
		choice = 5 
		player_spots[quadrant-1] = 2

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

def gameOverCheck():
	if player_spots[0] == 1:
		if (player_spots[1] == 1) and (player_spots[2] == 1):
			return False
	return True
			
def gameMenu():
	choice = int(input('Choose a spot (1-9): '))
	if player_spots[choice - 1] != 0:
		print('Spot in use')
	
	return choice

notGameOver = True

while notGameOver:
	printBoard()
	
	choice = gameMenu()
	player_spots[choice-1] = 1
	
	notGameOver = gameOverCheck()
	