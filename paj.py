# Print Fibbonaci numbers up to n
def fib(n):
	a, b = 0, 1
	while a < n:
		print(a)
		a, b = b, a+b
	return None

# For every number between 0 and n: if number can be divided by 3-print 'Fizz', by 5-print 'Buzz', by both - print 'FizzBuzz'
def fizzBuzz(n):
	for num in range(n+1):
		if num % 3 == 0:
			if num % 5 == 0:
				print(num, ' Fizzbuzz')
			else:
				print(num, ' Fizz')
		elif num % 5 == 0:
			print(num, ' Buzz')
		else:
			print(num)
	return None

# Print multiplication table of numbers up to n
def table(n):
	for num1 in range(n):
		for num2 in range(n):
			print(num1 * num2)
	return None
	

fib(10)
input()

fizzBuzz(30)
input()

table(4)
input()

			
