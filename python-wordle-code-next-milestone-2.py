import random
import sys

def main():
    # Get a random word.
    answer = getRandomWord()
    print(answer)

    # The game starts here.
    guess = ""
    attempts = 0

    while True:
        guess = input("Enter a 5 letter guess?\n")
        attempts += 1
        print("Guess #" + str(attempts) + ": " + guess)

# A method that gets a random word from a file.
def getRandomWord():
    # Read the file.
    file = open("words.txt", "r")

    # strip() removes the new line at the end of each word.
    words = []
    for word in file.readlines():
        word = word.strip()
        words.append(word)
    
    # choice() returns a randomly selected element from the input sequence or array.
    return random.choice(words)

main()
