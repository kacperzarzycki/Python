import re
# https://pl.spoj.com/problems/JGGHACK/ solution


def translate_G(letter):
	letters = {'B':'a', 'C':'b', 'D':'c', 'E':'d', 'F':'e', 'G':'f', 'H':'g', 'I':'h', 'J':'i', 'K':'j', 'L':'k', 'M':'l', 'N':'m', 'O':'n', 'P':'o'}
	return letters[letter]
def translate_H(letter):
	letters = {'A':'p', 'B':'q', 'C':'r', 'D':'s', 'E':'t', 'F':'u', 'G':'v', 'H':'w', 'I':'x', 'J':'y', 'K':'z'}
	return letters[letter]
try:
	coded_words = ['BGCGDGEGFGGGHGIGJGKG', 'LGBGEHBGDHEHCHPGGGBG', 'PGCGPGKHPGHHJGDHLGPG']
	for code in coded_words:
		# Separate long chain for list of all two character strings
		separated_code = list(re.findall(r'[A-Z][A-Z]', code))
		uncoded_letters = []
		for coded_letter in separated_code:
			x = list(coded_letter)
			if x[1] == 'G':
				uncoded_letters.append(translate_G(x[0]))
			else:
				uncoded_letters.append(translate_H(x[0]))
		print(''.join(uncoded_letters))
	input()
except Exception as exc:
	print(exc)
	input()