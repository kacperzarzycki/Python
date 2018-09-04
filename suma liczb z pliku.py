# Checks if file exists. If it doesn't, it will create one.
def check_file(): 
	try:
		with open('suma.txt', 'r') as CheckRead:
			None
	except:
		with open('suma.txt', 'w') as CheckWrite:
			None

# Returns sum of all integers (one per line) in text file
def sum_lines():
	with open('suma.txt', 'r') as file:
		allnumbers = []
		for line in file.readlines():
			try:
				line = int(line)
				allnumbers.append(line)
			except:
				print(line, ' is not correct\n')
	return sum(allnumbers)

check_file()
while True:
	print(sum_lines())
	input()

