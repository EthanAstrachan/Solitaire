import random

suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
numbers = ["A"] + [str(i) for i in range(2,11)] + ["J", "Q", "K"]

class Card():
	def __init__(self,cardId):
		self.suit = suits[cardId // 13]
		self.number = numbers[cardId % 13]
		self.color = "Red" if self.suit == "Hearts" or self.suit == "Diamonds" else "Black"

	def printCard(self):
		return (self.number + " of " + self.suit)

class Pile():
	cards = []
	bottomCard = 0
	topCard = 0

	def __len__(self):
		return len(self.cards)

	def create(self, cards):
		self.cards = cards
		self.bottomCard = len(self.cards)-1
		self.topCard = len(self.cards)-1

	def addCards(self, cards):
		if len(self.cards) == 0:
			self.create(cards)
			self.bottomCard = 0
		else:
			for card in cards:
				self.cards.append(card)
			self.topCard = len(self.cards) -1

	def removeCards(self):
		for i in range(self.topCard, self.bottomCard-1,-1):
			card = self.cards[i]
			self.cards.remove(card)
		self.bottomCard = len(self.cards)-1
		self.topCard = self.bottomCard

	def removeTop(self):
		card = self.cards[self.topCard]
		self.cards.remove(card)
		self.topCard -= 1
		if self.bottomCard == self.topCard + 1:
			self.bottomCard -=1

	def getTopCard(self):
		return self.cards[self.topCard]

	def getBottomCard(self):
		return [self.cards[i] for i in range(self.bottomCard, len(self.cards))]



class Solitaire():
	board = [Pile() for _ in range(7)]
	deck = [Card(i) for i in range(52)]
	pile = []
	foundation = {"Hearts": [], "Clubs": [], "Spades": [], "Diamonds": []}

	def createBoard(self):
		for i in range(len(self.board)):
			pile = []
			for _ in range(i+1):
				card = self.chooseCard()
				pile.append(card)
			self.board[i].create(pile)

		for _ in range(len(self.deck)):
			card = self.chooseCard()
			self.pile.append(card)

	def chooseCard(self):
		card = random.choice(self.deck)
		self.deck.remove(card)
		return card

	def printBoard(self):
		for col in range(7):
			cards = self.board[col].getBottomCard() if len(self.board[col]) > 0 else None
			if len(self.board[col]) > 0:
				print("Top of Stack " + str(col+1) + ": ", [card.printCard() for card in cards])
			else:
				print("Stack " + str(col+1) + " is empty")
		print("Top of pile: " + (self.pile[0].printCard() if len(self.pile) > 0 else "is empty"))
		for suit in self.foundation.keys():
			print(suit + " off the board: ", [card.printCard() for card in self.foundation[suit]])
		print("\n")

	def moveOnBoard(self,start, end):
		cardsToMove = self.board[start-1].getBottomCard()
		self.board[start-1].removeCards()
		self.board[end-1].addCards(cardsToMove)

	def moveToBoard(self, column):
		cardToMove = self.pile[0]
		self.pile.remove(cardToMove)
		self.board[column-1].addCards([cardToMove])

	def moveToFoundation(self, column):
		if(len(self.board[column-1]) > 0):
			card = self.board[column-1].getTopCard()
			key = card.suit
			self.foundation[key].append(card)
			self.board[column-1].removeTop()

	def moveToFoundationFromPile(self):
		if(len(self.pile) > 0):
			cardToMove = self.pile[0]
			self.pile.remove(cardToMove)
			key = cardToMove.suit
			self.foundation[key].append(cardToMove)


	def changePile(self):
		card = self.pile[0]
		self.pile.remove(card)
		self.pile.append(card)

	def winningBoard(self):
		for key in self.foundation.keys():
			if len(self.foundation[key]) != 13:
				return False
		return True

	def quit(self):
		return True

	def help(self):
		print("Here are the moves you can make:")
		print("moveOnBoard- moves a card or stack or cards from one pile to another. Takes two parameters, the pile moving from and the pile moving too")
		print("moveToBoard- moves from the remaining cards to a pile on the board. Takes one parameter, the pile moving to")
		print("moveToFoundation- moves a card to the foundation, which is where all cards should end up. Takes one parameter, the pile moving from")
		print("moveToFoundationFromPile- moves the card on top of the remaining pile to foundation. Takes no parameters")
		print("changePile- takes the top card on the remaining pile and moves it to the bottom. Takes no parameters")
		print("quit- exit game. Command should enter if game is unwinnable. Takes no parameters")
		print("help- see all possible moves")



if __name__ == "__main__":
	solitaire = Solitaire()
	solitaire.createBoard()
	print("Welcome To Solitaire! Type begin to play: ")
	playGame = input()
	if playGame == "begin":
		quit = False
		print("Here is the board: ")
		solitaire.printBoard()
		while not solitaire.winningBoard() and not quit :
			print("Make a move or type help to see moves")
			move = input().split(" ")
			function = move[0]
			if function == "help":
				solitaire.help()
			if function == "moveOnBoard":
				solitaire.moveOnBoard(int(move[1]), int(move[2]))
			if function == "moveToBoard":
				solitaire.moveToBoard(int(move[1]))
			if function == "moveToFoundation":
				solitaire.moveToFoundation(int(move[1]))
			if function == "moveToFoundationFromPile":
				solitaire.moveToFoundationFromPile()
			if function == "changePile":
				solitaire.changePile()
			if function == "quit":
				quit = solitaire.quit()
			if function != "help":
				solitaire.printBoard()
		if solitaire.winningBoard():
			print("Congratulations! You've won!")
		else:
			print("Sorry. Better luck next time")



