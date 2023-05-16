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


# Asks if user has played before (Display instructions if no)
played_before = yes_no("Have you played this game before?")

if played_before == "no":
    instructions()


# Number checking function goes here
def int_check(question, low=None, high=None, exit_code=None):
    if low is not None and high is not None:
        situation = "both"
        error = f"Please enter an integer between {low} and {high}"
    if low is None and high is None:
        situation = "any integer"
        error = "please enter an integer"
    else:
        error = f"please enter an integer more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:

            response = int(response)

            # checks input is not too high or too low if a both upper and lower bounds are specified
            if situation == "both":
                if low <= response <= high:
                    return response

            elif situation == "any integer":
                return response

            elif situation == "low only":
                if response >= low:
                    return response

            print(error)
            print("----------------------------")

        # checks input is an integer
        except ValueError:
            print(error)
            print("----------------------------")


# Main routine
rounds_played = 0
rounds_won = 0

mode = "regular"

print()
lowest = int_check("====Low Number====: ")
print("----------------------------")
highest = int_check("*****High Number*****: ", lowest + 1)
print("----------------------------")
rounds = int_check("====Rounds====: ", 1, exit_code="")
print("----------------------------")
guess = int_check("****Guess (or xxx to exit)****: ", lowest, highest, "xxx")

secret = random.randint(lowest, highest)

# rounds loop
end_game = "no"
while end_game == "no":
    if rounds == "":
        mode = "infinite"
        rounds = 5

    if mode == "infinite":
        heading = f"Rounds {rounds_played + 1} (infinite mode)"
        rounds += 1
    else:
        heading = f"Round {rounds_played + 1} of {rounds}"

    print(heading)

    rounds_played += 1

    while True:

        print("----------------------------")
        guess = int_check("****Guess (or xxx to exit)****: ", lowest, highest, "xxx")
        print("You guessed", guess)

        if guess == "xxx":
            end_game = "yes"
            break

    if rounds_played >= rounds:
        break
