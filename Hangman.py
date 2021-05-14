# Hangman
import random

words = ["mevil", "maxim", "prema", "maxim"]
random_word = random.choice(words) # choose a random word to guess
underscore_word = []  # adds "_" to some characters in random word

# adds each character of random word as an element in a list

underscore_word = [i for i in random_word] # using list comprehnesion to append to list
guessed_let = []  # keeps track of all guessed letters

#  Replaces random characters in word with "_" for user to guess
place = random.randint(2,5)
for elem in range(len(underscore_word)):
    if elem % place == 0:  # chooses a random spot for the user to guess so its not always the same
        underscore_word.remove(underscore_word[elem])  # removes the element at that spot
        underscore_word.insert(elem, "_")  # and replaces with a "_"

print("The underscore word is: ", underscore_word)

# Draws the hangman
def draw_game(guess_count):
  a = "_______"
  b = "|"
  print(a)
  for i in range(5):
    if guess_count == 1 and i == 0:
      print(b + "     " + b)
    elif guess_count == 2 and i == 0:
      print(b + "     " + "_" + b + "_ \n|    {___}")
    elif guess_count == 3 and i == 0:
      print(b + "     " + "_" + b + "_ \n|    {___}\n|      |\n|      |\n|      |\n|      |")
    elif guess_count == 4 and i == 0:
      print(b + "     " + "_" + b + "_ \n|    {___}\n|      |\n|     \|\n|      |\n|      |")
    elif guess_count == 5 and i == 0:
      print(b + "     " + "_" + b + "_ \n|    {___}\n|      |\n|     \|/\n|      |\n|      |")
    elif guess_count == 6 and i == 0:
      print(b + "     " + "_" + b + "_ \n|    {___}\n|      |\n|     \|/\n|      |\n|      |\n|     /")
    elif guess_count == 7 and i == 0:
      print(b + "     " + "_" + b + "_ \n|    {___}\n|      |\n|     \|/\n|      |\n|      |\n|     / \\")
    else:
      print(b)

guessed_word = ""
guess_count = 0  # tracks how many times user guessed wrong
repeat_let = []  # tracks if user repeated letters

# loops through the game until the word is guessed or the user lost
gameFlag = True
while gameFlag:
    user_guess = input("Guess the letter: ")
    user_guess = user_guess.lower()  # converts guess to lower case in case user enters upper case

    # checks if guessed word is in chosen word
    if user_guess in random_word:
        # loops through the word and checks the position of the guessed letter
        for i in range(len(random_word)):
            if user_guess == random_word[i]:
                underscore_word[i] = user_guess # changes the "_" to the guessed letter
        print("The word is: ", underscore_word)

    # if guessed letter is guessed again
    elif user_guess in guessed_let:
        print("You already used that letter.")

    # if guessed letter is not in word, draw the hangman
    else:
        guessed_let.append(user_guess)
        print("Sorry, wrong letter!\n")
        guess_count += 1
        # draw the hangman
        if guess_count == 1:
            draw_game(1)
        elif guess_count == 2:
            draw_game(2)
        elif guess_count == 3:
            draw_game(3)
        elif guess_count == 4:
            draw_game(4)
        elif guess_count == 5:
            draw_game(5)
        elif guess_count == 6:
            draw_game(6)
        elif guess_count == 7:
            draw_game(7)
            print("You lost the game.\n")
            gameFlag = False

    # if entire list is filled with letters, loop through and make it a string
    if "_" not in underscore_word:
        for j in underscore_word:
            guessed_word += j
        if guessed_word == random_word:
            print("You got the word: ", random_word)
            gameFlag = False  # stop while loop
