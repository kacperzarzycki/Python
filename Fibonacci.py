while True:
	x = int(input('How many Fibonacci numbers do You wish? ')) - 2
	try:
		a = 0
		print(a)
		if x > -1:
			b = 1
			print(b)
		for _ in range(x):
			c = a + b
			a = b
			b = c
			print(c)
		input()
	except Exception as exc:
		print(exc)
		input()