from os import system 
# Print player's stats
def print_info(money, lvl, eq, eqtobuy):
	system('cls')
	print('[-------------------------------]\n MONEY: {}\n LEVEL: {}\n \n\n\n {}\n\n You can buy:\n'.format(money, lvl, eq))
	for unittobuy in eqtobuy:
		print(unittobuy +'\n')
	return None

	# Count amount of elements of every kind separetly and return string with results
def count_army(eqlist):
	civilamount = eqlist.count('civil')
	policeamount = eqlist.count('police')
	thugamount = eqlist.count('thug')
	return str('civil[{}]   police[{}]   thug[{}]'.format(civilamount, policeamount, thugamount))

money = 0
lvl = 1
eqlist = []
eqtobuy = ['civil     50$      +2$', 'police    150$     +5$', 'thug      400$     +20$']
income = 1

while True:
	army = count_army(eqlist)
	print_info(money, lvl, army, eqtobuy)
	choice = input()
	# Check condition if player has enough money, if he does - add new eq, increase income and abjure cash
	if choice == 'civil' and money > 49:
		eqlist += ['civil']
		income += 2
		money -= 50
		lvl += 1
	elif choice == 'police' and money > 149:
		eqlist += ['police']
		income += 5
		money -= 150
		lvl += 3
	elif choice == 'thug' and money > 399:
		eqlist += ['thug']
		income += 20
		money -= 400
		lvl += 8
	# If player won't pick new eq, he gets money
	else:
		money += income
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
