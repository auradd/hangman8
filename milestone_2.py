# Step 1: Create a list of 5 favorite fruits
favorite_fruits = ['apple', 'banana', 'orange', 'kiwi', 'mango']

# Step 2: Assign the list to a variable called word_list
word_list = favorite_fruits

# Step 3: Print the list
print(word_list)

# Import the random module
import random

# Step 3: Create the random.choice method and pass the word_list variable into it
word = random.choice(word_list)

# Step 4: Assign the randomly generated word to a variable called word
word = random.choice(word_list)

# Step 5: Print out the word
print(word)

# Step 1: Ask the user to enter a single letter
guess = input("Enter a single letter: ")

# Step 2: Check if the input is a single alphabetic character
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")