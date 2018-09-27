def Fib(n):
		a, b = 0, 1
		while a < n:
			print(a)
			a, b = b, a+b
Fib(1000)
input()
