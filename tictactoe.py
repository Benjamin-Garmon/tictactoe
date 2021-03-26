# finding if someone won
def winner(lst):	
	champ = '_'
	for i in lst:
		# --- ways winner
		if len(set(i))==1 and '_' not in i:
			champ = i[0]
		# x ways winner
		elif (lst[0][0]==lst[1][1]==lst[2][2]) or lst[0][2]==lst[1][1]==lst[2][0]:
			champ = lst[1][1]
		# | ways winner
		else:
			for index , x in enumerate(i):
				if lst[0][index]==lst[1][index]==lst[2][index] and x!='_':
					champ = x
				
	if champ != '_':
		return champ
	elif '_' not in lst[0] and '_' not in lst[1] and '_' not in lst[2]:
		return 'Tie'

#printing the box that the x and o will show in 		
def show_game(lst):
	print(' _ _ _')
	for i, j in enumerate(lst):
			print('|' + '|'.join(lst[i]) + '|')

def play_game(lst):
	show_game(lst)
	game = True
	while game == True:
		# player 1 (X) placement

		while True:
			p1R = int(input('player1: row: '))-1
			p1C = int(input('player1: column: '))-1
			if lst[p1R][p1C]=='_':
				lst[p1R][p1C]='X'
				show_game(lst)
				break
			else:
				print('spot taken, try again')
				continue
		#check if X won (so you dont have to play the whole game before finding the winner if there is one)
		if winner(lst) == 'X':
			print("player 1 wins")
			game = False
			break
		elif winner(lst) == 'Tie':
			print("It's a Tie!!")
			game = False
			break
		#player 2 (O) placement
		while True:
			p2R = int(input('player2: row: '))-1
			p2C = int(input('player2: column: '))-1
			if lst[p2R][p2C]=='_':
				lst[p2R][p2C]='O'
				show_game(lst)
				break
			else:
				print('bad input, try again')
				continue
			#check if player 2 is the winner
			if winner(lst) == 'O':
				print("player 2 wins")
				game = False
				break
			elif winner(lst) == 'Tie':
				print("It's a Tie!!")

#starting list	
tictactoe = [['_','_','_'],['_','_','_'],['_','_','_']]
play_game(tictactoe)

