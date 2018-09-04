try:
	filename = input('file name and extention ')
	oldword = input('word to be changed ')
	newword = input('new word ')
	with open(filename, "r") as file:
		content = str(file.read())
	with open(filename, "w") as file:
		newcontent = content.replace(oldword, newword)
		file.write(newcontent)
	
except:
	print('Something went wrong')