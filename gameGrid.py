
import trie

#TODO: remove hardcoded grid size

MIN_WORD_LENGTH = 3

class gameGrid:
	def __init__(self, dictionaryTrie):
		self.grid = [[None for x in range(4)] for x in range(4)]
		self.boolGrid = [[False for x in range(4)] for x in range(4)]
		self.dictionaryRoot = dictionaryTrie
		self.foundWords = []

	def prettyPrint(self):
		height = len(self.grid)
		for i in range(height):
			print self.grid[i]

	def populate(self, letters):
		for x in range(0,16,4):
			self.grid[x/4] = list(letters[x:x+4])

	def searchGrid(self):
		self.foundWords = []
		for row in range(4):
			for column in range(4):
				self.findWords(row, column, self.dictionaryRoot)
		# Sort the found words by length of string before returning
		self.foundWords.sort(lambda x,y: cmp(len(x), len(y)))
		return self.foundWords

	def getGameCharacters(self):
		letters = raw_input("Enter all characters on grid left to right, row by row, each separated by a ',' :")
		#TODO: Check correct input
		self.populate(letters)

	def findWords(self, row, column, branch, word=[]):
		# check if letter has already been used before proceeding
		if self.boolGrid[row][column] == True:
			return

		letter = self.grid[row][column]
		num = ord(letter)-97
		# first check if branch exists for the letter, continue searching if so
		if branch.chars[num] != None:
			nextBranch = branch.getBranch(num)
			word.append(self.grid[row][column])
			self.boolGrid[row][column] = True
			if nextBranch.terminates == True and len(word) >= MIN_WORD_LENGTH:
				if ''.join(word) not in self.foundWords:
					self.foundWords.append(''.join(word))
			# recursively search clockwise on other letters
			if row > 0:
				self.findWords(row-1, column, nextBranch, word) #top
				if column < 3:
					self.findWords(row-1, column+1, nextBranch, word) #top right
			if column < 3:
				self.findWords(row, column+1, nextBranch, word) # right
				if row < 3:
					self.findWords(row+1, column+1, nextBranch, word) #bottom right
			if row < 3:
				self.findWords(row+1, column, nextBranch, word) #Bottom
				if column > 0:
					self.findWords(row+1, column-1, nextBranch, word) #Bottom Left
			if column > 0:
				self.findWords(row, column-1, nextBranch, word) # Left
				if row > 0:
					self.findWords(row-1, column-1, nextBranch, word) #Top Left


			#remove character from word list and boolean grid
			word.pop()
			self.boolGrid[row][column] = False
			return








tr = trie.trie()
tr.insertDictionary('words')
g = gameGrid(tr)


letters = 'dstvinhuierstecs'
#letters = raw_input('Enter letters from the grid: ')

g.populate(letters)
g.prettyPrint()

#g.findWords(0, 0, tr)
print g.searchGrid()

'''
g.foundWords.sort(lambda x,y: cmp(len(x), len(y)))
for word in g.foundWords:
	print word
'''
