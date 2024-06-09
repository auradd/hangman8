import random

# Create a list of words
word_list = ['apple', 'banana', 'orange', 'kiwi', 'mango']

# Randomly choose a word from the list
word = random.choice(word_list)

# Step 1: Create a while loop and set the condition to True
while True:
    # Step 2: Ask the user to guess a letter
    guess = input("Enter a letter: ")

    # Step 3: Check if the guess is a single alphabetic character
    if len(guess) == 1 and guess.isalpha():
        # Step 4: If the guess passes the checks, break out of the loop
        break
    else:
        # Step 5: If the guess does not pass the checks, print an error message
        print("Invalid letter. Please, enter a single alphabetical character.")

# Step 1: Check if the guess is in the word
if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")