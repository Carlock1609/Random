import random

rand_num = random.randrange(1,201)



def guess_game():
    total_guesses = 0
    guess = int(input("Please guess a number: "))

    while total_guesses < 11:
        if total_guesses == 10:
            print("You ran out of guesses!")
            break
        else:
            if guess == rand_num:
                total_guesses += 1
                print("You guessed the random number in " + total_guesses + " times!")
            if guess > rand_num:
                total_guesses += 1
                print("Your guess is to high!")
            if guess < rand_num:
                total_guesses += 1
                print("Your guess is to low!")

guess_game()
