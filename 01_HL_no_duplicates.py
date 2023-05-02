# HL component 5 - no duplicate1a

rounds = 6

secret = 7
guesses_allowed = rounds

already_guessed = []
guesses_left = guesses_allowed
num_won = 0

guess = ""

while guess != secret and guesses_left >= 1:

    guess = int(input("Guess: "))

    if guess in already_guessed:
        print("You already guessed that number🐵🐵 Please try again!")
        print("You 'still' have {} guesses left".format(guesses_left))

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < secret:
            print("Too low, try a higher number.\tGuesses left: {}".format(guesses_left))

        elif guess > secret:
            print("Too high, try a lower number.\tGuesses left: {}".format(guesses_left))
    else:
        if guess == secret:
            if guesses_left == guesses_allowed:
                print("Amazing! You got it")
            else:
                print("Well done, you got it!")
