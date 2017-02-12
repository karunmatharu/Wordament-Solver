#!/usr/bin/python
class trie:
	'''
	each node of the trie contains a list of 26 characters 
	and a terminator bool for strings which end at at this node
	'''
	def __init__(self):
		#print "creating a new trie"
		self.chars = [None]* 26
		self.terminates = False

	def insert(self, word):
		"""
		if no letters are left in word
		set the terminator character to True
		"""
		if len(word) <= 0:
			self.terminates = True
			return

		num = ord(word[0]) -97

		if self.chars[num] == None:
			self.chars[num] = trie()
			self.chars[num].insert(word[1:])
		else:
			# if leaf already exists for character
			self.chars[num].insert(word[1:])

		for letter in word:
			num = ord(letter) - 97
			if self.chars[num] == None:
				self.chars[num] == True


	def search(self, word):
		if len(word) <= 0:
			if self.terminates is True:
				return True
			else:
				return False
		num = ord(word[0]) -97
		if self.chars[num] != None:
			return self.chars[num].search(word[1:])
		else:
			return False


	'''
	Display elements in the trie using
	depth first traversal
	'''
	def printStrings(self, stack = []):
		if len(stack) > 0 and self.terminates == True:
			print ''.join(stack)
		for idx, character in enumerate(self.chars):
			if character is not None:
				# push the character onto the stack
				stack.append(unichr(idx + 97)) # get character from unicode
				character.printStrings(stack)
				stack.pop()


	def insertDictionary(self, filename):
		f = open(filename, 'r')
		lines = f.readlines()

		firstChar = '1'
		print 'Inserting Dictionary...'

		for l in lines:
			word = l.rstrip('\n')
			if word.isalpha() and word.islower():
				#for printing loading bar only
				if word[0] != firstChar:
					firstChar = word[0]
					print (firstChar)
				self.insert(word)
		print 'Completed'

	def getBranch(self, branchIndex):
		return self.chars[branchIndex]





