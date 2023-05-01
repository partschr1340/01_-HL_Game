import random

print(" * * * * Welcome to the HIGHER LOWER game * * * *")
print()


# Yes or no question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print()
            print("Please answer yes or no")
            print()


# Instructions to the game if user has not played before
def instructions():
    print()
    print(" For each game you will be asked to...")
    print()
    print("- Enter a 'low' and 'high' number, The computer will randomly")
    print("  generate a 'secret' numbers between your two chosen numbers.")
    print("  It will use these numbers for all the rounds in a given game.")
    print("- The computer will calculate how many guesses you are allowed.")
    print("- Enter the number of rounds you want to play")
    print("- Guess the secret number")
    print()
    print("Good Luck homie💩")


# Main routine
played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()
