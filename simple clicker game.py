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
	if lvl < 101:
		return str('civil[{}]   police[{}]   thug[{}]'.format(civilamount, policeamount, thugamount))
	soldieramount = eqlist.count('soldier')
	tankamount = eqlist.count('tank')
	chuckamount = eqlist.count('chuck')
	return str('civil[{}]   police[{}]   thug[{}]	soldier[{}]    tank[{}]    chuck[{}]'.format(civilamount, policeamount, thugamount, soldieramount, tankamount, chuckamount))
	

money = 0
lvl = 1
eqlist = []
eqtobuy = ['civil     50$      +2$', 'police    150$     +5$', 'thug      400$     +20$']
income = 1

while True:
	if lvl > 100:
		eqtobuy = ['soldier     7k$      +60$', 'tank    35k$     +170$', 'chuck      200k$     +800$']
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
	elif choice == 'soldier' and money > 6999:
		eqlist += ['soldier']
		income += 60
		money -= 7000
		lvl += 20
	elif choice == 'tank' and money > 34999:
		eqlist += ['tank']
		income += 170
		money -= 35000
		lvl += 60
	elif choice == 'chuck' and money > 199999:
		eqlist += ['chuck']
		income += 800
		money -= 200000
		lvl += 140
	# If player won't pick new eq, he gets money
	else:
		money += income
