import sys
import termcolor
import random

#creating the Wordle Class where all the code will be written
class Wordle:
    #Two class variables
    CurrentWord = ""
    NumberOfUserGuesses = 0

    #Here we take in two arguments and create the instance variables needed for the rest of the code
    def __init__(self, NumberofUserGuesses, FileName):
        self.guesses = NumberofUserGuesses
        self.file = FileName

    #Opening the text file which contains all the words and storing the words in a list
    def readFile(self):
        Lines = open("myWords.txt",'r')
        LinesAsWords = Lines.readlines()
        self.ListofWords = []
        for Element in range(len(LinesAsWords)):
            self.ListofWords.append(LinesAsWords[Element].rstrip())
        Lines.close()

    #Choosing a random word from the list
    def selectRandomWord(self):
        self.CurrentWord = random.choice(self.ListofWords)
        #prints the random word chosen and the length of the word
        # print(self.CurrentWord)
        # print(len(self.CurrentWord))

    #Deleting any additional spaces/characters that we don't want
    def removeNewLineFromWord(self):
        self.WordOfTheDay = self.CurrentWord.rstrip()

    def playWordle(self):
        #Starting at guess number one
        NumberOfUserGuesses = 1
        #Main loop which will run until the amount of guesses exceeds 6
        while NumberOfUserGuesses <= self.guesses:
            #storing input from user as a variable
            Guess = input("\n Guess Number {}:".format(NumberOfUserGuesses))
            #This "if" statement is to turn all the letters green and print the statement if the word is guessed also exit the while loop
            if Guess == self.WordOfTheDay:
                print(termcolor.colored(Guess, 'green'), end="")
                NumberOfUserGuesses += 1
                print("\n Congrats on getting today's wordle which was {}! you got it in {} tries".format(self.WordOfTheDay, NumberOfUserGuesses-1))
                NumberOfUserGuesses = self.guesses+1
            #Turning the letters green and yellow as needed and continuing the loop
            else:
                for i in range(len(self.WordOfTheDay)):
                    if Guess[i] == self.WordOfTheDay[i]:
                        print(termcolor.colored(Guess[i], 'green'), end="")
                    elif Guess[i] in self.WordOfTheDay:
                        print(termcolor.colored(Guess[i], 'yellow'), end="")
                    else:
                        print(Guess[i], end="")
                #Once the number of guesses exceeds 6 print statement
                if NumberOfUserGuesses == self.guesses:
                    print("\n You were not able to guess {} in {} tries. Try again!".format(self.WordOfTheDay, NumberOfUserGuesses))
                NumberOfUserGuesses += 1

#Code that instantiates your wordle class and runs it
game = Wordle(6, "myWords.txt")
game.readFile()
game.selectRandomWord()
game.removeNewLineFromWord()
game.playWordle()
