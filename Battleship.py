import random

class Battleship:

	def new_game(self, game_size, number_of_ships):
		self.game_size = game_size
		self.number_of_ships = number_of_ships
		if number_of_ships > game_size * game_size:
			raise Exception("Number should be below game_size")
		self._ship_location()

	def _ship_location(self):
		self.ship_location = {}
		counter = 0
		while counter < self.number_of_ships:
			m = random.randint(0, self.game_size -1)
			n = random.randint(0, self.game_size -1)
			if (m, n) not in self.ship_location:
				self.ship_location[(m,n)] = 'alive'
				counter += 1

	def guess(self, grid_location):

		for i in grid_location:
			if i > self.game_size:
				print("Out of Bound!")
				return


		if grid_location in self.ship_location:
			print ("Hit!")
			self.ship_location[grid_location] = False
		else:
			print ('Miss!')

		if 'alive' not in self.ship_location.values():
			print("Hit! You Win!")



game = Battleship()
game.new_game(3, 2)
# let's pretend the two ships get placed at grid locations (0,1) and (2,2)
game.guess((0,0)) # miss!
game.guess((0,1)) # hit!
game.guess((9,1)) # out of bounds!
game.guess((2,2)) # hit! You win!


