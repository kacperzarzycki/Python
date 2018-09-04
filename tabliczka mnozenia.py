def print_table(highestnumber):
	for x in range(1, highestnumber):
		print('\n')
		for y in range(1, highestnumber):
			print('{}*{} = {}'.format(x, y, x*y))

while True:
	try:
		highestnumber = int(input('range: ')) + 1
		print_table(highestnumber)
	except:
		print('Wrong input')
