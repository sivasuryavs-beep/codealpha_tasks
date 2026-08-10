import random

# List of predefined words
words = ["python", "apple", "laptop", "camera", "ocean"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong guesses
wrong_guesses = 0
max_wrong_guesses = 6

print("===================================")
print("      WELCOME TO HANGMAN GAME")
print("===================================")

while wrong_guesses < max_wrong_guesses:

    # Display the current progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter only one alphabet.")
        continue

    # Check if letter already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong Guess!")
        print("Remaining Chances:", max_wrong_guesses - wrong_guesses)

# If user loses
if wrong_guesses == max_wrong_guesses:
    print("\n💀 GAME OVER!")
    print("The correct word was:", word)

print("\nThank you for playing Hangman!")
