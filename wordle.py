import random
#creates a class Letter with fields value and position, this is used to track what letter a character is and its position in the word to guess
class Letter:
	def __init__(self, value, position):
		self.value = value
		self.position = position
#words.txt is where all posible words come from, all words are 5 letters. This file is used to pick a word and check if the users entry is a valid word
fin = open('words.txt')
#adds every word into a list and then generates a random number, and then selects a word which is stored at the
t = []
for line in fin:
	word = line.strip()
	t.append(word)	
length = len(t)
x = random.randint(0,length)
word_to_guess = t[x]

#For loop to iterate 6 times for 6 guesses
for guess_num in range(1,7):
	print("")
	print("Guess number", guess_num)
	guess = input("Enter a five letter word: ").lower()

	#checks if the guess is purley alphabetical, 5 letters long, and a valid word in list t in that order, checking if 'in t' last to be more efficent
	while (guess.isalpha() and len(guess) == 5 and guess.lower() in t) == False:
		guess = input("Try again: ")
	zxx = guess
	
	#Making a list of letter objects based on the guess
	objs = list()
	for i in range(len(guess)):
		objs.append(Letter(guess[i],i))

	#returns boolean value on how many times it is in the guess compared to the actual target word
	def in_twice(word_to_guess, letter_in_word, guess):
		return (guess.count(letter_in_word.value) > word_to_guess.count(letter_in_word.value) and letter_in_word.value in word_to_guess)




	for i in word_to_guess:
		pain = Letter(i,word_to_guess.index(i))
		if in_twice(word_to_guess, pain, guess):
			bad_letter = Letter(i,word_to_guess.index(i))
			break
		else:
			bad_letter = Letter("ã",0)


	"""finds the first and last location of duplicate letter in a word (if the letter is in the target word)
	 and if one is in the correct spot it will make sure that is handled by replacing the other with an a with an accent
	 this makes sure it still follows the .isalpha() but won't be in a legit wordle as it doesn't have accents
	"""
	def check(word_to_guess, letter_in_word, guess):
		new_guess = guess
		if in_twice(word_to_guess, letter_in_word, guess):
			x = guess.rfind(letter_in_word.value)
			z = guess.index(letter_in_word.value)
			if x == letter_in_word.position:
				new_guess = (guess[:z] + "ã" + guess[z+1:])
				return new_guess		
			else:
				new_guess = (guess[:x] + "ã" + guess[x+1:])
				return new_guess

		return new_guess


	new_guess = check(word_to_guess, bad_letter, guess)
	jobjs = list()

	#accesses both the index and value stored for new_guess and makes a list of letter objects composed of these values
	for idx, v in enumerate(new_guess):
		jobjs.append(Letter(str(v),idx))

	#Green for letter present in correct spot
	#Yellow for letter present in wrong spot
	#Red for letter not present
	for i in range(len(word_to_guess)):
		if (jobjs[i].value == word_to_guess[i]
			and jobjs[i].position == i):
			print("🟩", end="")
		elif jobjs[i].value in word_to_guess:
			print("🟨", end="")
		else:
			print("🟥", end="")
	
	#Handles the display of the ending of the game, either winning, or running out of guesses and losing
	if zxx == word_to_guess:
		print("")
		print("You guessed it! Congradulations 🎉🎈")
		break
	if guess_num == 6:
		print("")
		print("You lost :(, the word was", word_to_guess)
		break
	


