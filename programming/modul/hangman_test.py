from hangman import *
print "P1+++++++++++++++++++++++++++++++++++++++++P1"

print "isWordGuessed(secretWord, lettersGuessed)"
print "# False block #" 
print "T1:",isWordGuessed('apple', ['a', 'e', 'i', 'k', 'p', 'r', 's'])
print "T2:",isWordGuessed('mangosteen', ['s', 'h', 'b', 'l', 'z', 'k', 'n', 'm', 'i', 'd'])
print "T3:",isWordGuessed('broccoli', ['a', 'l', 's', 'd', 'y', 'm', 'j', 'e', 'f', 'x'])
print "T4:",isWordGuessed('lettuce', [])
print "# True block #" 
print "T5:",isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])
print "T6:",isWordGuessed('mangosteen', ['z', 'x', 'q', 'm', 'a', 'n', 'g', 'o', 's', 't', 'e', 'e', 'n'])

print "---------------------------------------------"

print "getGuessedWord(secretWord, lettersGuessed)"
print "# True block #" 
print "T1:",'_ pp_ e' == getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])
print "T2:",'durian' == getGuessedWord('durian', ['a', 'c', 'd', 'h', 'i', 'm', 'n', 'r', 't', 'u'])
print "T3:",'_ a_ _ ot' == getGuessedWord('carrot', ['f', 'a', 'v', 'm', 's', 'o', 'x', 'j', 't', 'k'])
print "T4:",'b_ _ _ _ _ _ _ ' == getGuessedWord('broccoli', ['g', 'h', 'z', 'e', 'b', 'u', 'q', 'j', 'n', 'a'])
print "T5:",'_ _ _ _ _ _ _ _ ' == getGuessedWord('broccoli', [])
print "T6:",'_ rocco_ _ ' == getGuessedWord('broccoli', ['k', 'j', 'r', 'p', 'o', 'd', 't', 'c', 'x', 'n'])

print "---------------------------------------------"

print "getAvailableLetters(lettersGuessed)"
print "# True block #" 
print "T1:",'abcdfghjlmnoqtuvwxyz' == getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])
print "T2:",'abcdefghijklmnopqrstuvwxyz' == getAvailableLetters([])
print "T3:",'bcefjknopqrsxz' == getAvailableLetters(['t', 'a', 'y', 'l', 'w', 'm', 'g', 'u', 'd', 'h', 'i', 'v'])
print "T4:",'acdfghjmopqrsz' == getAvailableLetters(['k', 'x', 'v', 't', 'e', 'b', 'y', 'n', 'w', 'i', 'l', 'u'])
print "T5:",'acdefhijklmnotvwyz' == getAvailableLetters(['u', 'b', 'g', 'x', 'q', 'r', 's', 'p'])
print "T6:",'bfhijloprstuxyz' == getAvailableLetters(['c', 'e', 'd', 'k', 'a', 'w', 'm', 'n', 'q', 'v', 'g'])

