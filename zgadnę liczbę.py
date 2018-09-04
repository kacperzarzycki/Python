import random
from os import system

# Program "zgadnie" liczbę którą wymyśliłeś
while True:
	input('pomyśl w głowie liczbę')
	system('cls')
	input('Właśnie tyle masz pieniędzy, a teraz dokładnie obliczaj')
	system('cls')
	input('Mama dała Ci tyle samo pieniędzy')
	system('cls')
	randomEvenNumber = random.randrange(3, 400) * 2
	input('ja daję Tobie {}zł'.format(randomEvenNumber))
	system('cls')
	input('Połowę wyrzucasz w błoto!')
	system('cls')
	input('Oddaj mamie dług')
	system('cls')
	input('Zostało Ci {}zł'.format(int(randomEvenNumber/2)))
	system('cls')
