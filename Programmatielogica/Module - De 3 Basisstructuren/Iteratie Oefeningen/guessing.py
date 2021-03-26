import random

result = random.randint(1, 100)
guesses = 0

while True:
    guess = int(input("Guess a number between 1 and 100."))
    guesses += 1
    if guess == result:
        break
    elif guess > result:
        print("Lower")
    else:
        print("Higher")

print("Correct! You guess a total of {} times.".format(guesses))
