import random

# Programme tests roulettes "Big Number" strategy which says:
# Bet 2$ on colour (for the first spin it can be black or red)
# Spin the wheel
# You win - change colour to the opposite and bet 2$ on it
# You lost - don't change colour, multiply bet by 2.
# You will never loose (until you have enough cash)


# Function generates random integer that represents pool's colour 	1=red 2=black 3=green 	and returns colour name 		
# Chance that green occurs is 1/37	chances that red or black occurs are 18/37
def get_colour():
	rand = random.randrange(1, 38)
	if rand <= 18:
		colournum = 1
	elif rand > 18 and rand <= 36:
		colournum = 2
	elif rand == 37:
		colournum = 3
	colours = {1: 'Red', 2: 'Black', 3: 'Green'}
	return colours[colournum]

# Return amount of cash for start. If input is incorrect cash = 100.
def get_cash():
	try:
		amount = int(input("Ile pieniędzy na start?"))
	except:
		print("100zł")
		amount = 100
	return amount
	
while True:
	cash = get_cash()	
	# games - games played, sum of all rounds
	# tour - sum of all lost rounds. Resets when player will win
	games, tour, picked_colour, bet = 0, 1, 'Red', 2
	
	print("Obstawiasz {}zł na kolor {}".format(bet, picked_colour)) 
	while cash > 0:
		#input()	# Uncomment that line if you want to click enter every tour
		colour = get_colour()
		#If player will win: change colour, get price (bet amount), set bet to 2
		if colour == picked_colour:
			if picked_colour == 'Red':
				picked_colour = 'Black'
			else:
				picked_colour = 'Red'
			cash += bet
			tour = 1
			games += 1
			bet = 2
			print('win')
		#If player will lose: pay bet, and increase next bet by two
		else:
			tour += 1
			games += 1
			cash -= bet
			bet = bet * 2
			print('lost')
		print("masz: {}zł	obstawiasz {}zł na kolor {}      tura: {} gier: {}".format(cash, bet, picked_colour, tour, games))
	input('Bankrut!')
	input()
