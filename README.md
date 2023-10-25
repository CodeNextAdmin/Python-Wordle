# Python-Wordle
The code for the Python Wordle workshop by Code Next. 
Python Wordle is meant to run as a Python script in the command line.

This repo contains 4 milestone files, featuring completed steps for each one. 

## Milestone 1 - Print a random word
How will we know what our answer (or Wordle word) is, each time our game is run?
The starter project has a words.txt file that we will pull our “random” word from.
We will use Python’s “open” function to read from this file, and add words to a list.
From this list, we will randomly choose our Wordle word! At this point, we will simply print the word to our console.

## Milestone 2 - Start the game loop
How does our game actually run, from the perspective of the player?
In this step, we will gather input from our player using the Python input function. This way we can store and analyze the user’s guess against our preselected Wordle word!

## Milestone 3 - Win or Lose?
How does our game know to end? How will the player know they are successful?
For this, we will use conditional statements.
IF the player has not found the correct answer, OR reached the allotted amount of attempts, the game should continue
 IF the player has found the correct answer, the game ends, and the player wins!
IF the player exceeds the maximum guesses (6) and has not found the answer, the game ends, and the player loses!
In either case, our console will print a message telling the player their result and what the answer was.

## Milestone 4 - Color the guesses
How can we make our game feel  like Wordle?
Hint: Even more loops and conditionals!
As we loop through our player input string, we compare each letter of the input to our preselected Wordle word. For each letter:
IF the letter in the guess is in the same spot as in the answer word, GREEN
IF the letter in the guess IS in the answer word, but in a different location, YELLOW
IF the letter in the guess is not in the answer word at all, OR is a duplicate of a previously colored letter which is NOT repeated in our answer word, RED
For example, if the answer word is ‘THREE’, and the user guesses ‘LEECH’, both ‘E’ letters should be yellow, because they belong in the word, but in different locations.
However, if the user guesses the word ‘ROGER’, our first ‘R’ will be yellow, because it is in the wrong location, but the second ‘R’ should be red, as the answer word does not contain multiple of that letter.
When engineers have completed the milestones, have them run their game! 
Be sure to go around and help with bug fixing. Try to help engineers understand WHY they are encountering bugs, rather than bug bashing FOR them.

