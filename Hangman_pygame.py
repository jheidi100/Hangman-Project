import pygame
import math
import random

# Setup. Don't modify
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman!")

WHITE = (255,255,255)
BLACK = (0,0,0)
RADIUS = 20

LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)

mode_rand_word = LETTER_FONT.render("Random Word", 1, BLACK)
pos_rand_word = (WIDTH/2 - mode_rand_word.get_width()/2, HEIGHT * 0.6)
                      
mode_enter_word = LETTER_FONT.render("Enter Your Own", 1, BLACK)
pos_enter_word = (WIDTH/2 - mode_enter_word.get_width()/2, HEIGHT * 0.7)

images = [pygame.image.load(f"images/hangman{i}.png") for i in range(7)]

FPS = 60
clock = pygame.time.Clock()
run = True

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def letter_position_dict(radius = RADIUS, gap = 15):
    output = dict()
    startx = round((WIDTH - 12 * gap - 26 * radius)/2)
    starty = round(HEIGHT * 0.8)   
    for i, letter in enumerate(alphabet):
        x = startx + (i%13)*(2*radius+gap) + radius
        y = starty + (i//13) * (2*radius+gap)
        output[letter] = (x,y)
    return output
        
letter_positions = letter_position_dict()


# State variables
screen = 0
hangman_status = 0
unused_letters = alphabet[:]
word_to_guess = "HELLO"
has_won = False

def initialize():
    global screen, hangman_status, unused_letters, word_to_guess, has_won
    screen = 0
    hangman_status = 0
    unused_letters = alphabet[:]
    word_to_guess = "HELLO"
    has_won = False

def display_word():
    output = ""
    for letter in word_to_guess:
        if letter not in unused_letters:
            output += letter + " "
        else:
            output += "_ "
    return output

def generate_random_word(word_list_file = "common_words.txt"):
    with open(word_list_file, "r") as f:
        word_string = f.read()
    return random.choice([word for word in word_string.split("\n") if len(word) > 3])

def draw_title():
    title = TITLE_FONT.render("HANGMAN", 1, BLACK)
    select_mode = WORD_FONT.render("Select Mode:", 1, BLACK)
    win.blit(title, (WIDTH/2 - title.get_width()/2, HEIGHT * 0.25))
    win.blit(select_mode, (WIDTH/2 - select_mode.get_width()/2, HEIGHT * 0.4))
    win.blit(mode_rand_word, pos_rand_word)
    win.blit(mode_enter_word, pos_enter_word)

def draw_letters():
    for letter in unused_letters:
        x,y = letter_positions[letter]
        pygame.draw.circle(win, BLACK, letter_positions[letter], RADIUS, 3)
        text = LETTER_FONT.render(letter, 1, BLACK)
        win.blit(text, (x-text.get_width()/2, y-text.get_height()/2))
        
def draw_word():
    text = WORD_FONT.render(display_word(), 1, BLACK)
    win.blit(text, (WIDTH/2, HEIGHT*0.4))
    

def draw():
    win.fill(WHITE)
    if screen == 0:
        draw_title()
    elif screen == 0.5:
        text = WORD_FONT.render("Enter word in console.", 1, BLACK)
        win.blit(text, (WIDTH/2 -  text.get_width()/2, HEIGHT/2))
    elif screen == 1:
        win.blit(images[hangman_status],(150,100))
        draw_letters()
        draw_word()
    elif screen == 2:
        win.blit(images[hangman_status],(150,100))
        draw_word()
        if has_won:
            text = WORD_FONT.render("YOU WIN!!!", 1, BLACK)
        else:
            text = WORD_FONT.render("YOU LOSE!!!", 1, BLACK)
            reveal_word = WORD_FONT.render(f"The word was {word_to_guess}.", 1, BLACK)
            win.blit(reveal_word, (WIDTH/2 - reveal_word.get_width()/2, HEIGHT * 0.9))
        win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT * 0.8))

def click_letter(m_x, m_y):
    global unused_letters, hangman_status
    for letter in unused_letters:
        x,y = letter_positions[letter]
        dist = math.sqrt((x-m_x)**2 + (y-m_y)**2)
        if dist <= RADIUS:
            unused_letters.remove(letter)
            if letter not in word_to_guess:
                hangman_status += 1
                break

def click_mode(m_x, m_y):
    global screen, word_to_guess
    if pos_rand_word[0] < m_x < pos_rand_word[0] + mode_rand_word.get_width()\
        and pos_rand_word[1] < m_y < pos_rand_word[1] + mode_rand_word.get_height():
        word_to_guess = generate_random_word().upper()
        screen += 1
        
    elif pos_enter_word[0] < m_x < pos_enter_word[0] + mode_enter_word.get_width()\
        and pos_enter_word[1] < m_y < pos_enter_word[1] + mode_enter_word.get_height():
        screen = 0.5
    

def check_win_lose():
    global screen, has_won
    if hangman_status == 6:
        screen += 1
        
    elif "_" not in display_word():
        has_won = True
        screen += 1
        
        


while run:
    clock.tick(FPS)
    
    draw()
    
    if screen == 0.5:
        word_to_guess = input("Enter word here: \n").upper()
        screen = 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if screen == 0:
                m_x, m_y = pygame.mouse.get_pos()
                click_mode(m_x, m_y)
            elif screen == 1:
                m_x, m_y = pygame.mouse.get_pos()
                click_letter(m_x,m_y)
                check_win_lose()
            elif screen == 2:
                initialize()
            
            
    pygame.display.update()
            
pygame.quit()