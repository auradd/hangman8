import random

# Create a list of words
word_list = ['apple', 'banana', 'orange', 'kiwi', 'mango']

# Randomly choose a word from the list
word = random.choice(word_list)

# Step 1: Define the check_guess function
def check_guess(guess):
    # Step 2: Convert the guess to lowercase
    guess = guess.lower()

    # Step 3: Check if the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Step 1: Define the ask_for_input function
def ask_for_input():
    # Step 2: Move the input validation code here
    while True:
        guess = input("Enter a letter: ")

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in list_of_guesses:
            print("You already tried that letter!")
        else:
            # Step 3: Call the check_guess function
            check_guess(guess)
            # Step 4: Append the guess to the list of guesses
            list_of_guesses.append(guess)
            break

# Initialize the list of guesses
list_of_guesses = []

# Step 4: Call the ask_for_input function
ask_for_input()