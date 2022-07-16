import random

WORDS = ["python", "java", "swift", "javascript"]
won = 0
lost = 0

def print_disguised(word, letters):
    for letter in word:
        if letter in letters:
            print(letter, end="")
        else:
            print("-", end="")
    print()


def see_results(won, lost):
    print(f"You won: {won} times.")
    print(f"You lost: {lost} times.")


def play():
    global won, lost
    word = random.choice(WORDS)
    attempts = 8
    letters = set(word)
    guessed_letters = set()
    wrong_letters = set()

    while attempts > 0:
        print()
        print_disguised(word, guessed_letters)
        letter = input(f"Input a letter:")
        if len(letter) != 1:
            print("Please, input a single letter..")
            continue
        elif letter.isalpha() and letter.isupper() or not letter.isalpha():
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        if letter in guessed_letters or letter in wrong_letters:
            print("You've already guessed this letter.")
            continue
        if letter in letters:
            guessed_letters.add(letter)
            if len(guessed_letters) == len(letters):
                print(f"You guessed the word {word}!")
                print("You survived!")
                won += 1
                break
        else:
            attempts -= 1
            wrong_letters.add(letter)
            print(f"That letter doesn't appear in the word.  # {attempts} attempts")
    else:
        print("You lost!")
        lost += 1

print("H A N G M A N  # 8 attempts")
while True:
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    command = input()
    if command == "exit":
        break
    elif command == "results":
        see_results(won, lost)
    elif command == "play":
        play()
    else:
        continue
