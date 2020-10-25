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
import random

def generate_random_word(word_list_file = "common_words.txt"):
    with open(word_list_file, "r") as f:
        word_string = f.read()
    return random.choice([word for word in word_string.split("\n") if len(word) > 3])

def print_win_message():
    print("CONGRATULATIONS! YOU WIN!")

def print_lose_message():
    print("SORRY, YOU ARE HANGED!")

def to_blanks(word):
    output = ""
    for letter in word:
        output += "-"
    return output

def combine(letter_list):
    output = ""
    for letter in letter_list:
        output += letter
    return output

def update_blanks(current_guess, word_to_guess, entered_letter):
    current_guess_list = list(current_guess)
    for i in range(len(word_to_guess)):
        if word_to_guess[i] == entered_letter:
            current_guess_list[i] = entered_letter
    return combine(current_guess_list)

def is_in_list(entered_letter, letter_list):
    for letter in letter_list:
        if entered_letter == letter:
            return True
    return False

def remove(items, to_remove):
    output = []
    for letter in items:
        if letter != to_remove:
            output.append(letter)
    return output


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

play_again = True



while play_again:
    print('LET\'S PLAY HANGMAN!\n')
    word_to_guess = input('Please enter a word for the other player to guess: ').upper()
    
    updated_guess = to_blanks(word_to_guess)
    num_guesses_left = int(input("Enter the number of guesses: "))
    
    unused_letters = alphabet[:]
    
    game_over = False
    
    while not game_over:
        print(f'\nGuess the word, {num_guesses_left} guess(es) left: {updated_guess}')
        print(f'Unused letters: {combine(unused_letters)}')
        
        if updated_guess == word_to_guess:
            print_win_message()
            game_over = True
            
        elif num_guesses_left == 0:
            print_lose_message()
            print(f"The word was {word_to_guess}.")
            game_over = True
        
        if game_over: 
            break
    
        new_letter = input().upper()
    
        if not is_in_list(new_letter, alphabet):
            print("Please enter a valid letter.")
            continue
         
        if not is_in_list(new_letter, unused_letters):
            print("Letter has already been guessed!")
            continue
            
        if is_in_list(new_letter, word_to_guess):
            updated_guess = update_blanks(updated_guess, word_to_guess, new_letter)
        else:
            num_guesses_left -= 1
            
        unused_letters = remove(unused_letters, new_letter)
    
    play_again = True if input("Play again? (Y/N)\n").lower() == "y" else False
    
