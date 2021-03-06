# Guess the Number

import random

def guess_game(number):
    ''' (int) -> None
    Prints if the user guessed the number or did not. '''

    gameFlag = True
    count = 0
    while gameFlag:
        user = int(input("Guess a number: "))
        if user == number:
            count += 1
            print("\nYou guessed it! It took you " + str(count) + " try('s)\n")
            gameFlag = False
        elif user > number:
            count += 1
            print("Your guess is higher than the number")
        elif user < number:
            count += 1
            print("Your guess is lower than the number")

print("\nWelcome to Guess the Number!\n")
userFlag = True
while userFlag:
    game_level = int(input("Choose a difficulty level: \n1) Easy (single digits) \n2) Medium (two digits) \n3) Hard (three digits)\n"
                           "Press 4 at any time to quit.\n"))
    if game_level == 1:
        number_easy = random.randint(0, 9)
        guess_game(number_easy)
    elif game_level == 2:
        number_med = random.randint(10, 99)
        guess_game(number_med)
    elif game_level == 3:
        number_hard = random.randint(100, 999)
        guess_game(number_hard)
    elif game_level == 4:
        print("\nThank you for playing the game.")
        userFlag = False
    else:
        print("Please enter an valid input\n")


