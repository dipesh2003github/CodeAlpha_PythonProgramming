import random

def hangman():
    words = ["python", "java", "flask", "numpy", "pandas","codealpha"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 10
    used_letters = []

    print("Welcome to Hangman!")
    while attempts > 0 and "_" in guessed:
        print("\nWord:", " ".join(guessed))
        print("Attempts left:", attempts)
        print("Used letters:", used_letters)

        guess = input("Guess a letter: ").lower()
        if guess in used_letters:
            print("Already guessed!")
            continue
        used_letters.append(guess)

        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print("Wrong guess!")

    if "_" not in guessed:
        print("You won! The word was:", word)
    else:
        print("Game over! The word was:", word)

hangman()