#Easygui guessing game by Les Pounder
import random
import easygui as eg

secret = random.randint(1,99)
guess = 0
tries = 0

eg.msgbox("Guess a number between 1 and 99, you have 6 tries")

while guess != secret and tries < 6:
    guess = eg.integerbox("What's your guess?")
    if not guess:
        break
    if guess < secret:
        eg.msgbox(str(guess) + " is too low")
    elif guess > secret:
        eg.msgbox(str(guess) + " is too high")
    tries = tries + 1

if guess == secret:
    eg.msgbox("You guessed correctly")
else:
    eg.msgbox("You have no more guesses left")
    eg.msgbox("The answer was " + str(secret))
