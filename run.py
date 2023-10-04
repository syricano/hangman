""" 
Program Planning Structure
1- I need a list to store words that will be used for secret guessing
2- select one word of the list randomly. and declare attempts
3- add input difficulty selection
4- ask player to make an input letters
5- validate the input to be a a letter not other types and keep prompting user
to make input if he incorrectly input something else
6- creating a function to check the letter if included in the secret word or if user input the whole letters of word
update the word index values if the input is correct 
if the input is incorrect to reduce attempts
7- create a function to represent the current status of guessing word or incorrect attempt 
( mainly drawing hangman symbols/character)
8- creating a function to check if user guessed the word to declare he winned
and ending the game, also if he lose
9 - add a function to allow user select difficulty which will be used to pick up the long words
in case of higher difficulty
10 - writing game rules.
11 - deploy the game to heroku after adding 2 build packs.
 
"""
import random
import os
import curses
import platform


easy_words = ['sun','cat', 'rat' ,'road', 'dog', 'rain', 'book', 'box', 'hat', 'car'
              'fish', 'key', 'word', 'game']
moderate_words = ["'apple", 'chair', 'earth', 'fruit', 'music', 'lemon', 'laptop',
                  'orange', 'summer', 'winter', 'window']
difficult_words = ['telephone', 'education', 'welcome', 'hospital', 'calender', 'butterfly',
                   'chocolate', 'mobility', 'computer', 'calculator ',
                   'letter', 'improvement', 'document']
attempts = 6

def clear_screen():
    """ 
    clear the terminal screen
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        
        

def choose_word(difficulty):
    """ 
    Prompt the user to select a difficulty level "easy, moderate, difficult"
    The function will pick up a word from each list
    """
    if difficulty == 'Easy':
        return random.choice(easy_words)
    elif difficulty == 'Moderate':
        return random.choice(moderate_words)
    elif difficulty == 'Difficult':
        return random.choice(difficult_words)

def display_hangman(stdscr, incorrect_guesses):
    """ 
    display the hangman drawing as per incorrect guesses
    """
    hangman = [
    "   ----   ",
    " |       |   ",
    " |       " + ("0" if incorrect_guesses > 0 else ""),
    " |      " + ("/" if incorrect_guesses > 2 else "") + ("|" if incorrect_guesses > 1 else "") + ("\\" if incorrect_guesses > 3 else ""),
    " |     " + ("/" if incorrect_guesses > 4 else "") + ("\\" if incorrect_guesses > 5 else ""),
    " |       ",
    "=========="
    ]
    for i, line in enumerate(hangman):
        stdscr.addstr(i, 0, line)

def display_word(stdscr, word, guessed_letters):
    """ 
    display the word with correctly guessed letters
    """
    display = ""
    for letter in word:
        if leeter in guessed_letters:
            display += letter
        else:
            display += "_"
    stdscr.addstr(7, 0, display)
    
def selected_difficulty(stdscr):
    """ 
    function to set the difficulty as per user input
    """
    stdscr.clear() # clear terminal screen
    stdscr.addstr(0, 0, "Welcome to Hangman Game !")
    stdscr.addstr(2, 0, "Choose a difficulty level:")
    difficulty_options = ["easy", "moderate", "difficult"]
    difficulty_index = 0
    
    while True:
        for i, option in enumerate(difficulty_options):
            if i == difficulty_index:
                stdscr.addstr(i + 4, 2, "->" + option)
            else:
                stdscr.addstr(i + 4, 2 , "  " + option)
                
        key = stdscr.getch()
        
        if key == curses.KEY_DOWN:
            difficulty_index = (difficulty_index + 1 ) % len(difficulty_options)
        elif key == curses.KEY_UP:
            difficulty_index = (difficulty_index - 1) % len(difficulty_options)
        elif key == 10: # Enter key
            return difficulty_options[difficulty_index]        

            
            
    
    

