import random
import os
import curses
import platform

# Lists of words for easy game
easy_words = [
    "code", "list", "word", "four", "tree", "bird", "pink", "frog",
    "jump", "leap", "rain", "book", "dark", "play", "time", "zone",
    "port", "gold", "star", "drop", "fish", "moon", "high", "open",
    "close", "love", "hate", "song", "race", "fast", "slow", "tall",
    "wall", "chip", "blue", "gray", "bark", "spin", "lamp", "heat",
    "bell", "well", "gold", "cold", "hand", "hope", "bold", "bond"
]

# Lists of words for moderate game
moderate_words = [
    "apple", "table", "chair", "house", "smile", "cloud", "green",
    "beach", "piano", "phone", "water", "music", "brush", "light",
    "happy", "tiger", "zebra", "dance", "earth", "lemon", "vivid",
    "beard", "grape", "sword", "ocean", "baker", "fancy", "quick",
    "juice", "sugar", "pizza", "puppy", "peace", "dream", "money",
    "peace", "grace", "train", "sunny", "pilot", "wrist", "laugh",
    "daisy", "smoke", "beard", "jelly", "candy", "happy", "lucky", "tulip"
]

# Lists of words for difficult game
difficult_words = [
    "freedom", "champion", "hospital", "elephant", "universe", "broccoli",
    "calendar", "computer", "keyboard", "mountain", "whisper", "language",
    "triangle", "eleven", "fantasy", "language", "synergy", "marathon",
    "boulevard", "magnolia", "beautiful", "sunshine", "friendly", "happiness",
    "knowledge", "inspired", "delicious", "ambitious", "vacation", "calendar",
    "wonderful", "victorious", "curiosity", "courageous", "celebrate",
    "basketball", "challenge", "celebration", "experience", "watermelon",
    "chocolate", "continuous", "community", "adventure", "creativity",
    "leadership", "innovation", "communication", "imagination"
]

# Numbers for allowed attempts
attempts = 6


def display_hangman(stdscr, incorrect_guesses):
    """
    Display the hangman drawing as per incorrect guesses
    """
    stdscr.addstr(8, 0, "Make a letter guess and save your man!")
    hangman = [
        "   ----   ",
        " |       |   ",
        " |       " + ("0" if incorrect_guesses > 0 else ""),
        " |      " + ("/" if incorrect_guesses > 2 else "") +
        ("|" if incorrect_guesses > 1 else "") +
        ("\\" if incorrect_guesses > 3 else ""),
        " |     " + (" /" if incorrect_guesses > 4 else "") +
        (" \\" if incorrect_guesses > 5 else ""),
        " |       ",
        "=========="
    ]
    for i, line in enumerate(hangman):
        stdscr.addstr(i, 0, line)


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


def display_word(stdscr, word, guessed_letters):
    """
    Update the guessed_word based on correctly guessed letters and return it.
    """
    guessed_word = [
        '_' if letter not in guessed_letters else letter for
        letter in word
    ]
    stdscr.addstr(10, 0, ' '.join(guessed_word))
    return guessed_word


def difficulty(stdscr):
    """
    Function to set the difficulty as per user input
    """
    # Clear terminal screen
    stdscr.clear()
    # Stdscr is the cursor window object to control users input and options
    stdscr.addstr(0, 0, "Welcome to Hangman Game!")
    stdscr.addstr(3, 0, "Choose a difficulty level:")
    difficulty_options = ["easy", "moderate", "difficult"]
    difficulty_index = 0
    # Iterating the difficulty lists and highlighting the selected one
    # with '->' before it
    while True:
        for i, option in enumerate(difficulty_options):
            if i == difficulty_index:
                stdscr.addstr(i + 4, 2, "->" + option)
            else:
                stdscr.addstr(i + 4, 2, "  " + option)
        # Method to control keyboard arrow keys up & down
        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            difficulty_index = (difficulty_index + 1) % len(difficulty_options)
        elif key == curses.KEY_UP:
            difficulty_index = (difficulty_index - 1) % len(difficulty_options)
        # Enter key (key == 10)
        elif key == 10:
            return difficulty_options[difficulty_index]


def display_rules(stdscr):
    """
    Display the game rules
    """
    rules = [
        "1. Choose a difficulty level: easy, moderate, or difficult.",
        "2. Guess letters to complete the hidden word.",
        "3. You have a limited number of attempts (6) to guess the word.",
        "4. If you guess a incorrect letter,part of the hangman will be drawn",
        "5. If you complete the word before running out of attempts, you win!",
        "6. If the hangman is fully drawn, you lose the game.",
        "7. You can play again or quit after each game."
    ]
    for i, rule in enumerate(rules):
        stdscr.addstr(i + 2, 0, rule)
    stdscr.addstr(10, 0, "Press 'Q' to go back to the main menu.")
    stdscr.refresh()
    while True:
        key = stdscr.getch()
        if key == ord('Q') or key == ord('q'):
            stdscr.clear()
            main(stdscr)
        elif key == 10:
            play_hangman_game(stdscr)


def play_hangman_game(stdscr):
    """
    Main game body with play again option
    """
    while True:
        # Calling functions, lists, and variables
        incorrect_letters = []
        try:
            curses.curs_set(0)
        except curses.error:
            pass
        selected_difficulty = difficulty(stdscr)
        word_to_guess = choose_word(selected_difficulty)
        guesses_letters = []
        incorrect_guesses = 0
        while True:
            stdscr.addstr(0, 0, "Difficulty: " + selected_difficulty)
            # Clear terminal screen
            stdscr.clear()
            stdscr.addstr(
                12, 0, "Incorrect letters: " +
                ', '.join(incorrect_letters)
            )
            # To check if the user entered letters correctly comparing them
            # with the original ones from the difficulty list.
            display_hangman(stdscr, incorrect_guesses)
            if display_word(stdscr, word_to_guess,
                            guesses_letters) == list(word_to_guess):
                stdscr.clear()
                stdscr.addstr(9, 0, "Congratulations! You guessed the word: " +
                              word_to_guess)
                stdscr.addstr(10, 0, "Press 'Y or Enter' to play again"
                              "or 'Q' to quit."
                              )
                stdscr.refresh()
                key = stdscr.getch()
                if key == ord('Y') or key == ord('y') or key == 10:
                    play_hangman_game(stdscr)
                elif key == ord('Q') or key == ord('q'):
                    stdscr.clear()
                    stdscr.addstr(0, 0, "Thanks for playing Hangman! Goodbye!")
                    stdscr.refresh()
                    # Display "Thanks" message for 3 seconds
                    curses.napms(3000)
                    exit(0)
                else:
                    stdscr.clear()
                    main(stdscr)

            guess = stdscr.getch()
            # Validating user's input to check if it's alphabetical
            # and converting it to lowercase
            if not chr(guess).isalpha():
                continue
            guess = chr(guess).lower()
            if guess in guesses_letters:
                continue
            elif guess in word_to_guess:
                # Append to guessed letters
                guesses_letters.append(guess)
            else:
                guesses_letters.append(guess)
                if guess not in word_to_guess:
                    incorrect_letters.append(guess)
                    incorrect_guesses += 1
            if incorrect_guesses >= attempts:
                display_hangman(stdscr, incorrect_guesses)
                # Ending the game
                stdscr.addstr(14, 0, "You ran out of attempts.")
                # Revealing the word
                stdscr.addstr(15, 0, "The word was : " + word_to_guess)
                stdscr.addstr(17, 0, "Press 'Y or Enter' to Play again"
                              "or 'Q' to quit."
                              )
                stdscr.refresh()
                stdscr.getch()
                key = stdscr.getch()
                if key == ord('Y') or key == ord('y') or key == 10:
                    stdscr.clear()
                    play_hangman_game(stdscr)
                elif key == ord('Q') or key == ord('q'):
                    stdscr.clear()
                    stdscr.addstr(0, 0, "Thanks for playing Hangman! Goodbye!")
                    stdscr.refresh()
                    # Display "Thanks" message for 3 seconds
                    curses.napms(3000)
                    exit(0)
                else:
                    stdscr.clear()
                    main(stdscr)


def main(stdscr):
    """
    Calling the game function
    """
    while True:
        stdscr.addstr(0, 0, "Welcome to Hangman Game!")
        stdscr.addstr(2, 0, "Select an option:")
        options = ["Play Game", "Rules", "Quit"]
        option_index = 0
        # Iterating the options and highlighting the selected one
        # with '->' before it
        while True:
            for i, option in enumerate(options):
                if i == option_index:
                    stdscr.addstr(i + 4, 2, "->" + option)
                else:
                    stdscr.addstr(i + 4, 2, "  " + option)
            # Method to control keyboard arrow keys up & down
            key = stdscr.getch()
            if key == curses.KEY_DOWN:
                option_index = (option_index + 1) % len(options)
            elif key == curses.KEY_UP:
                option_index = (option_index - 1) % len(options)
            elif key == 10:
                if options[option_index] == "Play Game":
                    play_hangman_game(stdscr)
                elif options[option_index] == "Rules":
                    display_rules(stdscr)
                elif options[option_index] == "Quit":
                    stdscr.clear()
                    stdscr.addstr(0, 0, "Thanks for playing Hangman! Goodbye!")
                    stdscr.refresh()
                    curses.napms(3000)
                    exit(0)

# Calling the main game in correspondence with the operating system


if __name__ == "__main__":
    if platform.system() == 'Windows':
        curses.wrapper(main)
    else:
        curses.wrapper(main)
