import re

try:
	while True:
		pairs_amount = int(input('Liczba par: '))
		answers = []
		for _ in range(pairs_amount):
			pair = input('')
			numbers = re.findall(r'[-+]?[0-9]+', pair)
			num1 = int(numbers[0])
			num2 = int(numbers[1])
			answer = num1 * num2
			answers.append(answer)
		for ans in answers:
			print(ans)
except Exception as exc:
	print(exc)
	input()