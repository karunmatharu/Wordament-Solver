
import trie
import re
import sys

MIN_WORD_LENGTH = 3
GRID_SIZE = 4

#TODO: three character tiles, clean code in findwords function

class Game:
	def __init__(self, dictionaryTrie):
		self.grid = [[None for x in range(GRID_SIZE)] for x in range(GRID_SIZE)]
		self.boolGrid = [[False for x in range(GRID_SIZE)] for x in range(GRID_SIZE)]
		self.dictionaryRoot = dictionaryTrie
		self.foundWords = []

	def prettyPrint(self):
		height = len(self.grid)
		for i in range(height):
			print self.grid[i]

	def populate(self, letters):
		splitLetters = letters.split()
		# convert all values to lowercase before populting grid
		for value in letters:
			value = value.lower()
		for row in range(GRID_SIZE):
			self.grid[row] = splitLetters[row*GRID_SIZE:(row*GRID_SIZE)+GRID_SIZE]
		print splitLetters

	def checkInput(self, letters):
		if letters.lower() == 'x':
			sys.exit()
		letters = letters.split()
		if len(letters) != GRID_SIZE**2:
			print '\nIncorrect input. There should be ' + str(GRID_SIZE**2) + ' values.'
			return False

		regexs = ["^\-?[A-z]{1,3}$" , "^[A-z]{1}\/[A-z]{1}$" ,  "^[A-z]{1,3}\-$"]
		for value in letters:
			if not any (re.match(regex, value) for regex in regexs):
				print '\n' + value + ' is not a valid tile value.'
				return False
		return True

	def searchGrid(self):
		self.foundWords = []
		for row in range(GRID_SIZE):
			for column in range(GRID_SIZE):
				self.findWords(row, column, self.dictionaryRoot)
		# Sort the found words by length of string before returning
		self.foundWords.sort(lambda x,y: cmp(len(x), len(y)))
		return self.foundWords

	def getGameCharacters(self):
		validInput = False
		while not validInput:
			letters = raw_input("\nEnter values of for tiles on grid left to right, " \
								"row by row, each separated by a space.\n" \
								"Or enter X to quit: \n") 
			validInput = self.checkInput(letters)
		self.populate(letters)

	def findWords(self, row, column, branch, word=None):
		if word:
			print 'word is ' + ''.join(word)
		print 'branch is ' + str(branch)

		if word == None:
			word = []
		# check if letter has already been used before proceeding
		if self.boolGrid[row][column] == True:
			return

		endingTile = False
		tile = self.grid[row][column]
		letterOptions = []
		# check if tile contains a dash for starting or ending tiles
		if '-' in tile:
			if tile.startswith('-'):
				endingTile = True
				letterOptions.append(tile[1:])
			elif tile.endswith('-'):
				# only proceed if this is the first tile
				if len(word) > 0:
					return
				letterOptions.append(tile[:-1])
		# check if a tile contains a '/' representing an either or 
		elif '/' in tile:
			letterOptions.append(tile[0])
			letterOptions.append(tile[2])
		else:
			letterOptions.append(tile)

		for letters in letterOptions: 
			# either/or tiles will have 2 options, all others will have 1
			nextBranch = branch
			for c in letters:
				print 'c is ' + c
				num = ord(c)-97
				if nextBranch:
					if nextBranch.getBranch(num) != None:
						nextBranch = nextBranch.getBranch(num)
					else:
						# return if branch for this character does not exist
						return
				else:
					return

			for c in letters:
				word.append(c)
			self.boolGrid[row][column] = True
			if nextBranch.terminates == True and len(word) >= MIN_WORD_LENGTH:
				if ''.join(word) not in self.foundWords:
					self.foundWords.append(''.join(word))
			
			if not endingTile:
				# recursively search clockwise on other letters
				if row > 0:
					self.findWords(row-1, column, nextBranch, word) #top
					if column < GRID_SIZE-1:
						self.findWords(row-1, column+1, nextBranch, word) #top right
				if column < GRID_SIZE-1:
					self.findWords(row, column+1, nextBranch, word) # right
					if row < GRID_SIZE-1:
						self.findWords(row+1, column+1, nextBranch, word) #bottom right
				if row < GRID_SIZE-1:
					self.findWords(row+1, column, nextBranch, word) #Bottom
					if column > 0:
						self.findWords(row+1, column-1, nextBranch, word) #Bottom Left
				if column > 0:
					self.findWords(row, column-1, nextBranch, word) # Left
					if row > 0:
						self.findWords(row-1, column-1, nextBranch, word) #Top Left
			# remove character(s) from word list and boolean grid
			for c in letters:
				word.pop()
			self.boolGrid[row][column] = False
		return

	def play(self):
		while True:
			self.getGameCharacters()
			self.prettyPrint()
			foundWords = self.searchGrid()
			for word in foundWords:
				print word






tr = trie.trie()
tr.insertDictionary('words')
game = Game(tr)
game.play()



