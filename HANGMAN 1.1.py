import random
import math
import urllib.request
wordlist = urllib.request.urlopen("https://www.gutenberg.org/files/2701/2701-0.txt")

WORDS = wordlist.read().split()

board =[" ____________",
     "|            |",
     "|            O",
     "|           /|^",
     "|            /^",
     "|",
     "____________", "last try !"]

b = 0
result= ""
empty = []
decomposedword =[]

def selectword():
    global result
    i = random.randint(0, 9999)
    guess = WORDS[i]
    w = len(guess)
    if w <= 3 or guess.isalpha() == False:
       return selectword()
    else:
        result = guess.decode('utf-8')
    
    
def setgame():
    global result
    global empty
    w = len(result)
    for x in range(w):
        empty.append(" _ ")
    

def keeptrack():
    global result
    global decomposedword 
    for letter in result:
        decomposedword.append(letter)
    

def startgame():
    global empty
    print ("Guess this word: {}".format(empty))

def wingame():
    global empty
    global result
    if " _ " not in empty:
        print ("Congratulation !!! Your word was indeed {}".format(result))
    else:
        return selectletter()

def loosegame():
    global b
    b += 1
    global result
    print (*board[0:b], sep = "\n")
    if b > 8 :
        print ("You loose ! Your word was {} !!!".format(result))
    else:
        return selectletter()
    

def selectletter ():
    x = input("Guess a letter : ")
    if x.isalpha() == False:
        print ("I said a  LETTER!")
        selectedletter = selectletter()
    else:
        selectedletter = x
    return compare(selectedletter)

def checkmultiple(a):
    global decomposedword
    if a in decomposedword:
        l = decomposedword.index(a)
        decomposedword[l] = "*"
        empty[l] = a
        return checkmultiple(a)
    else:
        print ("Good job ! {} is in the word !".format(a))
        print (empty)
        return wingame()
    

def compare(a):
    global decomposedword 
    global empty
    if a in decomposedword:
        l = decomposedword.index(a)
        decomposedword[l] = "*"
        empty[l] = a
        return checkmultiple(a)
    else :
        print ("No!")
        return loosegame()
        





selectword()
setgame()
keeptrack()
startgame()
selectletter()

