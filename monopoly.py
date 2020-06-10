import random

class Monopoly:
	def __init__(self):
		self.game = self._game()
		self.players = {}

	def add_player(self, name): #return or not?
		if name not in self.players:
			self.players[name] = [0, 500] #(location, sum)
			print(self.players)
		else:
			print("Name already existed. Try again.")

	def _game(self):
		game = {}
		nums = (-200, 50)
		for i in range(1, 41):
			game[i] = random.choice(nums)
		return game

	def turn(self, name):
		dice = random.randint(1, 6)
		self.players[name][0] += dice
		if self.players[name][0] > 40:
			self.players[name][0] -= 40
		self.players[name][1] += self.game[self.players[name][0]]

		if self.players[name][1] <=0:
			print("You lost!")
		else:
			print(self.players)






game = Monopoly()
game.add_player("Yuna")
game.add_player("Aaron")
game.add_player("Yuna")
game.turn("Yuna")
game.turn("Yuna")
game.turn("Yuna")
game.turn("Yuna")
game.turn("Yuna")
game.turn("Yuna")
game.turn("Yuna")


