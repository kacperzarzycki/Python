from datetime import datetime
import os

# Sprawdzenie czy plik dziennik.txt istnieje. Jeśli nie istnieje - stworzenie
try:
    diary_file = open('dziennik.txt', 'r')
    diary_file.close()
except:
    diary_file = open('dziennik.txt', 'w')
    diary_file.close()


while True:
    # Odczyt całości w odwróconej kolejności
    with open('dziennik.txt', 'r') as diary_content:
        for line in reversed(list(diary_content)):
            print(line)

    # Nadpisanie pliku (data, temat, wcześniejsza zawartość), pominięcie, lub exit
    topic = input("n/Dziś: ")
	# Jeśli wybrano 'n', doda się datestamp - nowy dzień do pliku dziennik.txt
    if topic == 'n':
        diary_content = open('dziennik.txt', 'r').read()
        diary = open('dziennik.txt', 'w')
        diary.write(str(datetime.now().strftime('%m-%d')+'----------------------------' + '\n' + diary_content))
        diary.close()
	# Inny wybór to temat wpisany do dziennik.txt
    elif topic != '' :
        diary_content = open('dziennik.txt', 'r').read()
        diary = open('dziennik.txt', 'w')
        diary.write(str('    - ' + '    ' + topic + '\n' + diary_content))
        diary.close()
    os.system('cls')
