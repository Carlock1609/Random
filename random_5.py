#! python3

import random

# get user to enter in letter

def get_random_num():

    return random.randint(0,10)

def get_guess():

    return int(input("Please enter in a number 1-10: "))

def replay():

    play_again = input("Do you want to play again?: (Yes or No?)").lower()

    if play_game == "yes":
        game_on = True
    else:
        game_on = False


while True:

    play_game = input("Do you want to guess my number 1-10?: (Yes or No)")

    if play_game.lower() == "yes":
        game_on = True
    else:
        game_on = False

    while game_on:
        guess = get_guess()
        num_guessed = []
        secret_num = get_random_num()

        if guess != secret_num:
            num_guessed.append(guess)
        else:
            replay()
