try:
	# Return last number only
	def return_last(number):
		numbers = list(str(number))
		return numbers[-1]
	
	def power(base, exponent):
		power_answer = base ** exponent
		return power_answer
		
	def get_numbers():
		base = int(input('base: '))
		exponent = int(input('exponent: '))
		return base, exponent
		
	while True:
		base, exponent = get_numbers()
		answer = power(base, exponent)
		print(return_last(answer))
except Exception as exc:
	print(exc)
	input()