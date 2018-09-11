# For (0=<'a', 'b'<10) of 'a b' input compare which is grater

try:
	# separate numbers
	def separate(word):
		characters = list(word)
		first_number = int(characters[0])
		second_number = int(characters[-1])
		return first_number, second_number
	
	# Compare numbers. If they are equal return 0, if first is greater return 1, if second is greater return 2
	def compare(first_number, second_number):
		if first_number == second_number:
			return 0
		elif first_number > second_number:
			return 1
		elif first_number < second_number:
			return 2
		else:
			return None

	while True:
		first_number, second_number = separate(input('x y: '))
		print(compare(first_number, second_number))
except Exception as exc:
	print(exc)
	input()