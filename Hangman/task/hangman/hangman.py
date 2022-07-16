import random

WORDS = ["python", "java", "swift", "javascript"]


print("H A N G M A N")
word = random.choice(WORDS)
test = input("Guess the word")
if test == word:
    print("You survived!")
else:
    print("You lost!")
