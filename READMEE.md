#_Hangman_

# Introduction

[Hangman](https://github.com/syricano/hangman) is a website for the classical hangman game that can be played online. It can be played [here]##to be added after deployed 

## Technologies used
- [python](https://www.python.org/) the programming language used to create this game.
- [VScode](https://code.visualstudio.com/) was the editor used to write my codes.
- [Lucidchart](https://lucid.app/lucidchart/fa9b2743-5bf5-4d84-9b61-a6478f78a67f/edit?viewport_loc=-634%2C-65%2C2466%2C1223%2C0_0&invitationId=inv_c279b1c0-6d04-4edb-acc5-1f045c1c60c4)


### User stories:

1- As a player, I want to be able to select a difficulty level (easy, moderate, difficult) at the beginning of the game so that I can choose the level of challenge I prefer.
2- As a player, I want to see a visual representation of the hangman as I make incorrect guesses, so I can track my progress and avoid losing.
3- As a player, I want to be able to see the incorrect letters I've guessed so far, so I can avoid repeating them.
4- As a player, I want to see the current status of the word I'm trying to guess, with blanks for letters I haven't guessed yet, so I can better guess the word.
5- As a player, I want to know if my guess is correct and see the updated word if I guessed correctly, so I can continue making progress.
6- As a player, I want to know if my guess is incorrect and see the hangman drawing progress if I guessed wrong, so I can keep track of my remaining attempts.
7- As a player, I want to be informed  if I win the game by correctly guessing the word, so I can celebrate my victory.
8- As a player, I want to be notified if I lose the game by running out of attempts, so I can see the correct word and decide to play again.
9- As a player, I want the option to play the game again after either winning or losing, so I can continue playing without restarting the program.
10- As a player, I want to access the game rules to understand how to play, so I can learn or refresh my knowledge of the game.
11- As a player, I want to have the option to quit the game if I decide to exit, so I can gracefully exit the program.
12- As a developer, I want to deploy the game to Heroku with the necessary build packs so that players can access it online.

---


- bugs: conflict between function name selection_difficulty and varible selcted_difficulty

resolved by rename the function
- game when running an error occur due to missing () for lowercase of guess word.
it was resolved by adding ()

- a bug found that nothing print when the word is guessed
it was resolved by assigning variable to guessed word and comparing it with word to guess (secret word)

- a bug found in rules, it did not quite when selecting q, 

resolved adding the forgotten parentheses 