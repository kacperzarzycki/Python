from datetime import datetime
import os

# Sprawdzenie czy plik dziennik.txt istnieje. Jeśli nie istnieje - stworzenie
try:
    diaryfile = open('dziennik.txt', 'r')
    diaryfile.close()
except:
    diaryfile = open('dziennik.txt', 'w')
    diaryfile.close()


while True:
    # Odczyt całości w odwróconej kolejności
    with open('dziennik.txt', 'r') as diarycontent:
        for line in reversed(list(diarycontent)):
            print(line)

    # Nadpisanie pliku (data, temat, wcześniejsza zawartość), pominięcie, lub exit
    topic = input("n/Dziś: ")
	# Jeśli wybrano 'n', doda się datestamp - nowy dzień do pliku dziennik.txt
    if topic == 'n':
        diarycontent = open('dziennik.txt', 'r').read()
        diary = open('dziennik.txt', 'w')
        diary.write(str(datetime.now().strftime('%m-%d')+'----------------------------' + '\n' + diarycontent))
        diary.close()
	# Inny wybór to temat wpisany do dziennik.txt
    elif topic != '' :
        diarycontent = open('dziennik.txt', 'r').read()
        diary = open('dziennik.txt', 'w')
        diary.write(str('    - ' + '    ' + topic + '\n' + diarycontent))
        diary.close()
    os.system('cls')
