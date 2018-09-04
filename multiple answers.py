def get_answer():
	answer = input("Do you love python?")
	if answer in ('y', 'yes', 'Yes'):
		return "That's great!"
	elif answer in ('n', 'no', 'No'):
		return "Oh god! Why?!"
	else:
		print("I don't know that answer")
		
while True:
	print(get_answer(), '\n')
