# this code is for a simple number guessing game 

import random

print("Hello! What is your name?")
name = input()

print("Well, " + name + " I am thinking of a number between 1 and  20.")
secretnumber = random.randint(1,20)

for guessestaken in range(1,6):
    print("Take a guess.")
    guess=int(input())

    if guess<secretnumber:
        print("Your guess is too low.")
    elif guess>secretnumber:
        print("Your guess is too high.")
    elif guess==secretnumber:
        print("Good job, " + name + "! You guessed my number in " + str(guessestaken) + " guesses!")
        break

if guess != secretnumber:
    print("Sorry, the number I was thinking of was " + str(secretnumber) + ".")
print("You took " + str(guessestaken) + " guesses.")

while True:
    print("Do you want to play again? (yes/no)")
    answer = input()
    if answer.lower() == "yes":
        secretnumber = random.randint(1,20)
        for guessestaken in range(1,6):
            print("Take a guess.")
            guess=int(input())

            if guess<secretnumber:
                print("Your guess is too low.")
            elif guess>secretnumber:
                print("Your guess is too high.")
            elif guess==secretnumber:
                print("Good job, " + name + "! You guessed my number in " + str(guessestaken) + " guesses!")
                break

        if guess != secretnumber:
            print("Sorry, the number I was thinking of was " + str(secretnumber) + ".")
        print("You took " + str(guessestaken) + " guesses.")
    elif answer.lower() == "no":
        print("Thank you for playing! Goodbye!")
        break
    else:
        print("Please answer with 'yes' or 'no'.")