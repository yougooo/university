# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import re
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print "Loading word list from file..."
    # inFile: file
    f = open(WORDLIST_FILENAME, 'rU',0)
    # line: string
    data = f.read()
    # wordlist: list of strings
    #wordlist = string.split(line)
    data = data.split()
    #print "  ", len(data), "words loaded."
    return data

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

#my help, fix some bug in my code 
def letter(letter,lettersGuessed):
    if letter in lettersGuessed: return letter
    return '_'

def guess(secretWord,letter):
    """
    letter : it is choise user one char
    """
    if letter in secretWord:
        print 'good guess'
        return True
    print 'bed guess'
    return False
# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0 
    for letter in secretWord:
        if letter in lettersGuessed:
            count = count + 1 
        if count == len(secretWord):
            return True
    return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return ''.join(map(lambda x: letter(x,lettersGuessed),secretWord)) 

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    if len(lettersGuessed) == 0:
        return string.ascii_lowercase
    return re.sub('{0}'.format(lettersGuessed),'',string.ascii_lowercase)

def hangman(secretWord):
    '''

    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    main = True
    count = 0
    lettersGuessed = []
    print 'We have {0} letters in secret word'.format(len(secretWord))
    while main:
        print '-----------------------------'
        print 'Raund {} start'.format(count)
        print 'Availadle letters is {0}'.format(getAvailableLetters(lettersGuessed))
        temp = raw_input('Enter one letter: ')
        if temp not in getAvailableLetters(lettersGuessed):
                print 'not valid letter, please make your choice from {0}'.format(getAvailableLetters(lettersGuessed))
                continue
        else:
                lettersGuessed.append(temp)
        #print getGuessedWord(secretWord, lettersGuessed)
        if guess(secretWord,temp):
                count = count - 1
        print getGuessedWord(secretWord, lettersGuessed)
        count = count + 1
        if isWordGuessed(secretWord, lettersGuessed):
                print '-----------------------------'
                print 'you win'
                print '-----------------------------'
                break
        elif count == 8:
                print '-----------------------------'
                print 'game over'
                print 'your word was {0}'.format(secretWord)
                print '-----------------------------'
                break
        


hangman(chooseWord(wordlist))
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
