while True:
	try:
		x = int(input('Prime numbers from 0 to: '))
		if x > 1:
			print(2)
		for number in range(x+1):
			for divider in range(2, number):
				if number % divider == 0:
					break
				if number % divider !=0 and divider==number-1:
					print(number)
	except:
		print('Please insert an integer number')