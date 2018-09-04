import time
from os import system

h = int(input("ile godzin? "))
m = int(input("ile minut? "))
s = int(input("ile sekund? "))

# time sum in seconds
s = s + 60*(m + (60 * h))

while s > 0:
	time.sleep(1)
	s -= 1

	secondsleft = s
	minutesleft = 0
	hoursleft = 0
	# Convert seconds to minutes and seconds
	while secondsleft>=60:
		secondsleft -= 60
		minutesleft += 1
	# Convert minutes and seconds to hours, minutes and seconds
	while minutesleft >= 60:
		minutesleft -= 60
		hoursleft += 1

	system('cls')
	print ("godzin:         minut:     sekund: \n")
	print ("  {}              {}          {}".format(hoursleft, minutesleft, secondsleft))
input("czekam")
