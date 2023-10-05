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


easy_words = ['sun','cat', 'rat' ,'road', 'dog', 'rain', 'book', 'box', 'hat', 'car', 
              'fish', 'key', 'word', 'game'] # lists of words for easy game
moderate_words = ['apple', 'chair', 'earth', 'fruit', 'music', 'lemon', 'laptop',
                  'orange', 'summer', 'winter', 'window'] # lists of words for moderate game
difficult_words = ['telephone', 'education', 'welcome', 'hospital', 'calendar', 'butterfly',
                   'chocolate', 'mobility', 'computer', 'calculator ',
                   'letter', 'improvement', 'document'] # lists of words for difficult game
attempts = 6 # numbers for allowed tempts 

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
    if difficulty == 'easy':
        return random.choice(easy_words)
    elif difficulty == 'moderate':
        return random.choice(moderate_words)
    elif difficulty == 'difficult':
        return random.choice(difficult_words)

def display_hangman(stdscr, incorrect_guesses):
    """ 
    display the hangman drawing as per incorrect guesses
    """
    stdscr.clear() # clear terminal screen
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
        Update the guessed_word based on correctly guessed letters and return it.
    """
    guessed_word = ['_' if letter not in guessed_letters else letter for letter in word]
    stdscr.addstr(7, 0, ' '.join(guessed_word))
    return guessed_word
    
    
def difficulty(stdscr):
    """ 
    function to set the difficulty as per user input
    """
    stdscr.clear() # clear terminal screen
    # Stdscr is the curser window object to control users input and options
    stdscr.addstr(0, 0, "Welcome to Hangman Game !")
    stdscr.addstr(2, 0, "Choose a difficulty level:")
    difficulty_options = ["easy", "moderate", "difficult"]
    difficulty_index = 0
    
    while True: #iterating the difficulty lists and highlighting the selected one with -> before it 
        for i, option in enumerate(difficulty_options):
            if i == difficulty_index:
                stdscr.addstr(i + 4, 2, "->" + option)
            else:
                stdscr.addstr(i + 4, 2 , "  " + option)
                
        key = stdscr.getch() # method to control keyboard arrow keys up & down
        
        if key == curses.KEY_DOWN:
            difficulty_index = (difficulty_index + 1 ) % len(difficulty_options)
        elif key == curses.KEY_UP:
            difficulty_index = (difficulty_index - 1) % len(difficulty_options)
        elif key == 10: # Enter key
            return difficulty_options[difficulty_index]        

def play_hangman_game(stdscr):
    """ 
    main game body with play again option
    """
    while True:
        """ 
        calling functions , lists and variables"""
        incorrect_letters = []
        curses.curs_set(0)
        stdscr.clear() # clear terminal screen
        selected_difficulty = difficulty(stdscr)
        word_to_guess = choose_word(selected_difficulty)
        guesses_letters = []
        incorrect_guesses = 0
        
        while True:
            
            stdscr.addstr(0, 0, "Difficulty: " + selected_difficulty)
            stdscr.addstr(9, 0, "Incorrect letters: " + ', '.join(incorrect_letters)) # display incorrect letters
            display_hangman(stdscr, incorrect_guesses)
                    
            if display_word(stdscr, word_to_guess, guesses_letters) == list(word_to_guess): # to check if user entered letters correctly comparing it with original one from difficulty list
                stdscr.addstr(9, 0, "Congratulations! You guessed the word: " + word_to_guess)
                stdscr.addstr(10, 0, "Press 'Y' to play again or 'Q to quite")
                stdscr.refresh()
                key = stdscr.getch()
                if key == ord('Y') or key == ord('y'):
                    break
                else:
                    return
            
            guess = stdscr.getch()
            
            if not chr(guess).isalpha(): #validating users input to check if it's alphabetical and converts it to lowercase >below method
                continue
            
            guess = chr(guess).lower()
            
            if guess in guesses_letters:
                continue
            elif guess in word_to_guess:
                guesses_letters.append(guess) # append to guessed letters
            
            else:
                guesses_letters.append(guess)
                if guess not in word_to_guess:
                    incorrect_letters.append(guess) #append to incorrect letters list
                    incorrect_guesses += 1  
                    
                
                
            if incorrect_guesses >= attempts:
                stdscr.clear()
                display_hangman(stdscr, incorrect_guesses)
                stdscr.addstr(9, 0, "You ran out of attempts.") #ending the game
                stdscr.addstr(10, 0, "The word was : " + word_to_guess) #reveling the word
                stdscr.addstr(11, 0, "Press 'Y' to Play again or 'Q' to quite.")
                stdscr.refresh()
                stdscr.getch()
                key = stdscr.getch()
                if key == ord('Y') or key == ord('y'):
                    break
                else:
                    return
def main(stdscr):
    """ 
    calling game function 
    """
    while True:
        play_hangman_game(stdscr)
        stdscr.addstr(12, 0, "Thanks for playing Hangman !")
        stdscr.refresh()
        key = stdscr.getch()
        if key == ord('Q') or key == ord('q'):
            break
        
        
# Calling the main game in corresponding with operating system
if __name__== "__main__":
    if platform.system() == 'windows':
        curses.wrapper(main)
    else:
        curses.wrapper(main)          
            
            
        
            
            
    
    

