# HL component 1 - Get (and check) user input
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


# Asks if user has played before (Display instructions if no)
played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()


# Number checking function goes here
def int_check(question, low=None, high=None):
    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:

            response = int(input(question))

            # checks input is not too high or too low if a both upper and lower bounds are specified
            if situation == "both":
                if response < low or response > high:
                    print(f"Please enter a number between {low} and {high}")
                    continue

            elif situation == "low only":
                if response < low:
                    print(f"Please enter a number that is more than (or equal to) {low}")
                    continue

            return response

        # checks input is an integer
        except ValueError:
            print()
            print("please enter an integer")
            print()
            continue


# Main routine
rounds_played = 0

print()
lowest = int_check("====Low Number====: ")
print("----------------------------")
highest = int_check("*****High Number*****: ", lowest + 1)
print("----------------------------")
rounds = int_check("====Rounds====: ", 1, exit_code="")
print("----------------------------")
guess = int_check("****Guess****: ", lowest, highest)

mode = "regular"

