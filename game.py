import random

# Step 1: Predefined words
words = ["python", "apple", "banana", "orange", "mango"]

# Step 2: Randomly choose a word
secret_word = random.choice(words)

# Step 3: Store guessed letters
guessed_letters = []

# Step 4: Number of lives
lives = 6

print("===== HANGMAN GAME =====")

# Step 5: Game Loop
while lives > 0:

    print("\nWord: ", end="")

    correct = True

    # Display word
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_ ", end="")
            correct = False

    print()

    # Check Win
    if correct:
        print("\n🎉 Congratulations! You guessed the word.")
        break

    # User Guess
    guess = input("Enter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Correct or Wrong
    if guess in secret_word:
        print("✅ Correct Guess!")
    else:
        lives -= 1
        print("❌ Wrong Guess!")
        print("Remaining Lives:", lives)

# Lose Condition
if lives == 0:
    print("\n💀 Game Over!")
    print("The word was:", secret_word)