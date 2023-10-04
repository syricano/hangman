""" 
Program Planning Structure
1- I need a list to store words that will be used for secret guessing
2- select one word of the list randomly. and declare attempts
3- ask player to make an input letters
4- validate the input to be a a letter not other types and keep prompting user
to make input if he incorrectly input something else
5- creating a function to check the letter if included in the secret word or if user input the whole letters of word
update the word index values if the input is correct 
if the input is incorrect to reduce attempts
6- create a function to represent the current status of guessing word or incorrect attempt 
( mainly drawing hangman symbols/character)
7- creating a function to check if user guessed the word to declare he winned
and ending the game, also if he lose
8 - add a function to allow user select difficulty which will be used to pick up the long words
in case of higher difficulty
9 - writing game rules.
10 - deploy the game to heroku after adding 2 build packs.
 
"""

Easy_Words = ['sun','cat', 'rat' ,'road', 'dog', 'rain', 'book', 'box', 'hat', 'car'
              'fish', 'key', 'word', 'game']
Moderate_words = ["'apple", 'chair', 'earth', 'fruit', 'music', 'lemon', 'laptop',
                  'orange', 'summer', 'winter', 'window']
Difficult_Words = ['telephone', 'education', 'welcome', 'hospital', 'calender', 'butterfly',
                   'chocolate', 'mobility', 'computer', 'calculator ',
                   'letter', 'improvement', 'document']
import random
attempts = [6]


print("Welcome to Hangman Game")
