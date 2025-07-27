import random
words = ["apple", "table", "chair", "phone", "house"]
word = random.choice(words)
guessed_letters = []
attempts_left = 6

print("Welcome to Hangman!")

while attempts_left > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    
    print("Word:", " ".join(display_word))

    if "_" not in display_word:
        print("Congratulations! You guessed the word.")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in word:
        guessed_letters.append(guess)
        print("Good guess!")
    else:
        guessed_letters.append(guess)
        attempts_left -= 1
        print("Wrong guess! Attempts left:", attempts_left)

if attempts_left == 0:
    print("Game Over! The word was:", word)