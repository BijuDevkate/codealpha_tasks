import random

stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\  |
         |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    """
]

words = ["python", "banana", "guitar", "orange", "rocket"]
word = random.choice(words)

guessed = []
display = ["_"] * len(word)
wrong = 0

while wrong < 6 and "_" in display:
    print(stages[wrong])
    print("Word:", " ".join(display))
    print("Guessed:", " ".join(guessed))

    guess = input("Enter a letter: ").lower()

    if guess in guessed:
        print("Already guessed")
    elif guess in word:
        guessed.append(guess)
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
    else:
        guessed.append(guess)
        wrong += 1

    print()

print(stages[wrong])

if "_" not in display:
    print("You won! The word was", word)
else:
    print("You lost! The word was", word)
