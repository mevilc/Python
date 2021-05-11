# TicTacToe
import random

# makes an empty board
board=["-"] * 9

def printboard():
    ''' (None) -> None
    Print the TicTacToe board '''
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# prints the empty board
printboard()

def computers_turn(computer_pos):
    ''' (List) -> None
    Takes a list and removes all the computer guesses from it.
     '''
    computer_guess = random.choice(computer_pos)  # computer randomly chooses a position from the available positions

    # if that position on board is not already used, assign a "O" in that position
    if board[computer_guess] != "X":
        board[computer_guess] = "O"
        computer_pos.remove(computer_guess)  # remove that position from available positions so that the computer cannot choose it again
        print("\nCOMPUTER'S TURN")
        printboard() # prints board with computer guess
    else:
        computers_turn(computer_pos)  # if not, calls function recursively, until an empty spot is found

def userwon():
    ''' (None) -> Bool
    Checks if user (X) won in any given condition. If user did not win, returns False '''

    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        print("User won1!")
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        print("User won2!")
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        print("User won3!")
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        print("User won4!")
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        print("User won5!")
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        print("User won6!")
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("User won6!")
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        print("User won6!")
    else:
        return False

def computerwon():
    ''' (None) -> Bool.
    Checks if computer (Y) won in any given condition. If computer did not win, returns False'''

    if board[0] == "O" and board[1] == "O" and board[2] == "O":
       print("Computer won!")
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        print("Computer won!")
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        print("Computer won!")
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        print("Computer won!")
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        print("Computer won!")
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        print("Computer won!")
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        print("Computer won!")
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        print("Computer won!")
    else:
        return False

###################### MAIN CODE #####################

used_pos = []  # tracks all the spots used by user
computer_pos=[0,1,2,3,4,5,6,7,8]  # all available spots for the computer to choose from

def playgame():
    ''' (None) -> None
    Main function that calls other functions '''
    play_game = True

    # loops through the game
    while play_game:
        user_input = int(input("Enter an option from 0 to 8: "))

        # checks if user input is not already used and its a valid input
        if user_input not in used_pos and str(user_input) in "012345678":
            board[user_input] = "X" # prints "X" to that spot
            used_pos.append(user_input) # adds that user input to the used_pos so that the user does not repeat it
            printboard() # prints board with user input
            if userwon() is False: # if user did not win, let computer play
                computers_turn(computer_pos)
            else: # if user wins, stop loop
                play_game = False

        # if user input is not valid
        elif str(user_input) not in "012345678":
            print("Please enter a valid input.")

playgame()