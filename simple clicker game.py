from os import system 
# Print player's stats
def print_info(money, lvl, eq, eqToBuy):
	system('cls')
	print('[-------------------------------]\n MONEY: {}\n LEVEL: {}\n \n\n\n {}\n\n You can buy:\n'.format(money, lvl, eq))
	for unitToBuy in eqToBuy:
		print(unitToBuy +'\n')
	return None

	# Count amount of elements of every kind separetly and return string with results
def count_army(eqList):
	civilAmount = eqList.count('civil')
	policeAmount = eqList.count('police')
	thugAmount = eqList.count('thug')
	return str('civil[{}]   police[{}]   thug[{}]'.format(civilAmount, policeAmount, thugAmount))

money = 0
lvl = 1
eqList = []
eqToBuy = ['civil     50$      +2$', 'police    150$     +5$', 'thug      400$     +20$']
income = 1

while True:
	army = count_army(eqList)
	print_info(money, lvl, army, eqToBuy)
	choice = input()
	# Check condition if player has enough money, if he does - add new eq, increase income and abjure cash
	if choice == 'civil' and money > 49:
		eqList += ['civil']
		income += 2
		money -= 50
	elif choice == 'police' and money > 149:
		eqList += ['police']
		income += 5
		money -= 150
	elif choice == 'thug' and money > 399:
		eqList += ['thug']
		income += 20
		money -= 400
	# If player won't pick new eq, he gets money
	else:
		money += income
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
