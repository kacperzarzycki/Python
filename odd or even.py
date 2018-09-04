from os import system
def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False


while True:
	try:
		number = int(input("Give me a number. I will check if it is odd or even\n"))
		system('cls')
		if is_even(number):
			print(number, ' is even\n')
		else:
			print(number, ' is odd\n')
	except:
		system('cls')
		print('Something went wrong. Pleae give me an integer number.\n')
		input('Press enter to continue')
		system('cls')

	
    
    
    
