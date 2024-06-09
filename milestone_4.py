import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)  # Pick a random word from the word_list
        self.word_guessed = ['_'] * len(self.word)  # Create a list of underscores with the same length as the word
        self.num_letters = len(set(self.word))  # Set of unique letters in the word
        self.num_lives = num_lives  # Number of lives the player has
        self.word_list = word_list  # List of words
        self.list_of_guesses = []  # List of guesses made by the player

    def check_guess(self, guess):
        guess = guess.lower()  # Convert the guess to lowercase
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            # Replace the underscores with the guessed letter
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1  # Reduce the number of unique letters
        else:
            self.num_lives -= 1  # Reduce the number of lives
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        while True:
            guess = input("Enter a letter: ")

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break