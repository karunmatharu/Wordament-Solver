import re

'''
pattern = re.compile("[A-z]")
print re.match("^[A-z]{1,2}$","aaaaaa")
'''
regs = ["^\-?[A-z]{1,2}$" , "^[A-z]{1}\/[A-z]{1}$" ,  "^[A-z]{1,2}\-$"]

letters = 'e a e1 m m r ghe- o o de- a t l m s l'
letters = letters.split()

for x in range(len(letters)):
	print any (re.match(regex, letters[x]) for regex in regs)
