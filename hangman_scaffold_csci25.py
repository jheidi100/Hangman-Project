# Landon Porter R. Browning, 190729
# Sarah D. Rivers, 201104
# Christopher Q. Egret, 190012
# October 26, 2020

# I/we certify that this submission complies with the DISCS Academic Integrity
# Policy.

# If I/we have discussed my/our Python language code with anyone other than
# my/our instructor, my/our groupmates, the teaching assistants,
# the extent of each discussion has been clearly noted along with a proper
# citation in the comments of my/our program.

# If any Python language code or documentation used in my/our program
# was obtained from another source, either modified or unmodified, such as a
# textbook, website or another individual, the extent of its use has been
# clearly noted along with a proper citation in the comments of my/our program.

################################################################################

# print message when player wins
def print_win_message():
    print("CONGRATULATIONS! YOU WIN!")

# print message when player loses
def print_lose_message():
    print("SORRY, YOU ARE HANGED!")

# a string of blanks (hyphens) equal in length to word
# examples:
    # if word is 'DOG' then to_blanks will return '---'
    # if word is 'HEART' then to_blanks will return '-----'
    # if word is 'PINEAPPLE' then to_blanks return make '---------'
def to_blanks(word):
    pass # replace pass with the appropriate instructions

# concatenates each letter in a list to form one string
# example: ['A', 'B', 'C'] returns 'ABC'
def combine(letter_list):
    pass # replace pass with the appropriate instructions

# returns a string where the
# hyphens are replaced with the corresponding letter
# whenever the player inputs a correct letter
# (i.e. a letter that occurs in the word)
# example:
    # the word to guess is 'CHOCOLATE'
    # the player has currently guessed 'CH-C---T-'
    # the player then inputs the letter 'O'
    # this should result in 'CH-C---T-' becoming 'CHOCO--T-'
def update_blanks(current_guess, word_to_guess, entered_letter):
    pass # replace pass with the appropriate instructions

# checks if a letter is in a list
# examples:
    # list is ['A', 'B', 'C'] and player enters letter 'B'
    # then the function returns True
    
    # list is ['A', 'B', 'C'] and player enters letter 'E'
    # then the function returns False
def is_in_list(entered_letter, letter_list):
    pass # replace pass with the appropriate instructions

# removes all elements in list equal to to_remove
# example:
    # list is ['A', 'B', 'C'] and player enters letter 'B'
    # then the function returns the list ['A', 'C']
def remove(items, to_remove):
    pass # replace pass with the appropriate instructions

print('LET\'S PLAY HANGMAN!\n')

# ask player for word to be guessed
print('Please enter a word for the other player to guess:')
word = input()

updated_guess = to_blanks(word)
num_guesses_left = 6
unused_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
used_letters = []

# initialize win and lose variables to False
win = False
lose = False

# game proper
# replace False with the appropriate condition/expression
while False: # keep looping until the outcome has been determined
    print(f'\nGuess the word, {num_guesses_left} guess(es) left: {updated_guess}')
    print(f'Unused letters: {combine(unused_letters)}')

    # ask player for letter
    new_letter = None # replace None with the appropriate code

    # decide what to do based on input
    # replace False with the approriate condition/expression
    # replace pass with the appropriate instructions
    if False: # when chosen letter has been previously used
        pass # print appropriate message
    elif False: # when input is not a letter in the alphabet
        pass # print appropriate message
    elif False: # when chosen letter occurs in word to be guessed
        pass # update the list of used and unused letters
             # and update the blanks (hyphens)
    else: # what to do when chosen letter does not occur in word to be guessed
        pass # update the list of used and unused letters
             # and update the number of guesses left

    # replace False with the appropriate condition/expression
    win = False # expression that determines if the guessing player has won
    lose = False # expression that determines if the guessing player has lost

# when loop ends, print appropriate output
if win:
    pass # replace pass with the appropriate instructions
elif lose:
    pass # replace pass with the appropriate instructions
