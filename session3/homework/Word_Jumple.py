import string
import random

word = "champion"

jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
print(jumble)

guess = input("Your guess: ")
if guess == "champion":
    print("Correct")
else:
    print("Try again")
