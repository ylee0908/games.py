from random import randint


class Hangman:
	words = ["apple", "banana", "pear", "tomato", "watermelon"]
	attempt = 10


	def __init__(self):
		self.display = []
		self.choose_answer()
		self.used_word = []
		self.wrong_guesses = 0
		while not self.is_game_over():
			self.draw_hangman()
			self.display_answer()
			guess = self.user_guess()
			self.process_guess(guess)

	def choose_answer(self):
		chosen_int = randint(0, 4)
		self.answer = self.words[chosen_int]
		for i in range(0, len(self.answer)):
			self.display.append('_')

	def draw_hangman(self):
		print("No of wrong guesses: ", self.wrong_guesses)

	def display_answer(self):
		print(" ".join(self.display))

	def user_guess(self):
		while self.wrong_guesses < self.attempt:
			guess = input("Enter your guess: ")
			if len(guess) !=1:
				print("Enter one letter at a time. Try again.")
			else:
				return guess.lower()

	def process_guess(self, letter):
		if letter in self.used_word:
			print("You already guessed it. Try again.")
		elif letter in self.answer:
			for i in range(len(self.answer)):
				if self.answer[i] == letter:
					self.display[i] = letter
			self.used_word.append(letter)
			return
		else:
			self.wrong_guesses += 1
			self.used_word.append(letter)
		return


	def is_game_over(self):
		if self.wrong_guesses == self.attempt:
			print ("You lost!")
			return True
		else:
			if str("".join(self.display)) == self.answer:
				print("You won!")
				return True
			else:
				return False



game = Hangman()

