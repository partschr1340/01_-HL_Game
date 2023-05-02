# HL component 1 - Get (and check) user input
import random

print(" * * * * Welcome to the HIGHER LOWER game * * * *")
print()


# Yes or no question, whether user has  played the game before or not
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


# Number checking function goes here
def int_check(question, low=None, high=None):
    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:
        try:

            response = int(input(question))

            # checks input is not too high or too low if a both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print()
                    print("Please enter a number between {} and {}".format(low, high))
                    print()
                    continue

            elif situation == "low only":
                if response < low:
                    print()
                    print("Please enter a number that is more than (or equal to) {}".format(low))
                    print()
                    continue

            return response

        # checks input is an integer
        except ValueError:
            print()
            print("please enter an integer")
            print()
            continue


# Main routine

print()
lowest = int_check("====Low Number====: ")
print("----------------------------")
highest = int_check("*****High Number*****: ", lowest + 1)
print("----------------------------")
rounds = int_check("====Rounds====: ", 1)
print("----------------------------")
guess = int_check("****Guess****: ", lowest, highest)

# Asks if user has played before (Display instructions if no)
played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()


