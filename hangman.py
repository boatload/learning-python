import random

# List of words to choose from for the game
WORDS = ["apple", "banana", "orange", "grape", "strawberry"]

# Select a random word from the list
word = random.choice(WORDS)

# Initialize the game state
guessed_letters = []
lives = 6

while True:
    # Print the current game state
    for letter in word:
        if letter in guessed_letters:
            print(letter, end="")
        else:
            print("_", end="")
    print("")
    print(f"Lives: {lives}")

    # Get the player's guess
    guess = input("Guess a letter: ")

    # Check if the guess is correct
    if guess in word:
        print("Correct!")
        guessed_letters.append(guess)
    else:
        print("Incorrect!")
        lives -= 1

    # Check if the game is over
    if lives == 0:
        print("Game over! The word was:")
        print(word)
        break
    elif all(letter in guessed_letters for letter in word):
        print("You win! The word was:")
        print(word)
        break
