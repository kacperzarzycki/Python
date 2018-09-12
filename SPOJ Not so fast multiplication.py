import re

try:
	while True:
		pairs_amount = int(input('Liczba par: '))
		if pairs_amount > 1000:
			raise Exception('Too high value')
		answers = []
		for _ in range(pairs_amount):
			pair = input('')
			numbers = re.findall(r'[-+]?[0-9]+', pair)
			num1 = int(numbers[0])
			num2 = int(numbers[1])
			if num1 > 99999:
				raise Exception('Too high value')
			if num2 > 99999:
				raise Exception('Too high value')
			answer = num1 * num2
			answers.append(answer)
		for ans in answers:
			print(ans)
except Exception as exc:
	print(exc)
	input()