# Imports
import random
from os import system, name

# Funcion Clear Console


def clearConsole():

    # Windows
    if name == "nt":
        _ = system('cls')

    # Unix
    else:
        _ = system('clear')


# End Function Clear Console

# Define Const Board

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

# End Define Const Board


# Class Game


class Hangman():

    # Constructor method

    def __init__(self, word):

        self.word = word
        self.wrongLetters = []
        self.choiceLetters = []

    # End Constructor method

    # Letter guessing method

    def guess(self, letter):

        if letter in self.word and letter not in self.choiceLetters:
            self.choiceLetters.append(letter)

        elif letter not in self.word and letter not in self.wrongLetters:
            self.wrongLetters.append(letter)

        else:
            return False

        return True

    # End Letter guessing method

    # Check end game method

    def hangmanOver(self):

        return self.hangmanWon() or (len(self.wrongLetters) == 6)

    # End Check end game metod

    # Check if the player has won method

    def hangmanWon(self):

        if "_" not in self.hideWord():
            return True
        return False

    # End Check if the player has won method

    # Hide letter in the board method

    def hideWord(self):

        rtn = ''

        for letter in self.word:
            if letter not in self.choiceLetters:
                rtn += '_'
            else:
                rtn += letter

        return rtn

    # End Hide letter in the board method

    # Check game status method

    def printGameStatus(self):

        print(board[len(self.wrongLetters)])

        print("\nWords: " + self.hideWord())

        print("\nWrong Letters: ",)

        for letter in self.wrongLetters:
            print(letter,)

        print()

        print("Correct Letters: ",)

        for letter in self.choiceLetters:
            print(letter,)

        print()

    # End Check game status method


# End Class Game


# Function chooses random word


def randWord():

    words = ["banana", "avocado", "grape", "strawberry", "orange"]

    word = random.choice(words)

    return word


# End Function chooses random word


# Bloco main


def main():

    clearConsole()

    game = Hangman(randWord())

    while not game.hangmanOver():

        game.printGameStatus()

        userInput = input("Enter a letter: ")

        game.guess(userInput)

    game.printGameStatus()

    if game.hangmanWon():
        print("Congratulations! You win!!!")

    else:
        print("Game Over! You lose!!!")
        print("The word was: " + game.word)


# End Bloco main

if __name__ == "__main__":
    main()
