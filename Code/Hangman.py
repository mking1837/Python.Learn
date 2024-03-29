import random

wordlist = ['grape', 'melon', 'chair', 'table', 'brush', 'pasta', 'shirt', 'pants', 'shoes', 'socks', 'watch', 'phone', 'mouse', 'paper', 'books', 'apple', 'mango', 'peach', 'lemon', 'berry', 'onion', 'radis', 'beets', 'beans', 'steak', 'pizza', 'bread', 'train', 'plane', 'boats', 'bikes', 'jeeps', 'sedan', 'coupe', 'wagon', 'truck', 'David', 'James', 'Henry', 'Sarah', 'Alice', 'piano', 'clock']
word = random.choice(wordlist)
guess =  '*****'

import random
import turtle
turtle.pensize(5)
errors=0
def showStickman():
    if (errors==1):
        turtle.bk(100)
        turtle.fd(200)
    if (errors==2):
        turtle.bk(100)
        turtle.lt(90)
        turtle.fd(300)
    if (errors==3):
        turtle.rt(90)
        turtle.fd(150)
    if (errors==4):
        turtle.rt(90)
        turtle.fd(50)
    if (errors==5):
        turtle.dot(50)
        turtle.fd(100)
    if(errors==6):
        turtle.bk(75)
    if (errors==7):
        turtle.rt(45)
        turtle.fd(50)
        turtle.bk(50)
    if (errors==8):
        turtle.lt(90)
        turtle.fd(50)
        turtle.bk(50) 
    if (errors==9):
        turtle.rt(45)
        turtle.fd(75)
        turtle.rt(45)
        turtle.fd(50)
        turtle.bk(50)
    if (errors==10):
        turtle.lt(90)
        turtle.fd(50)
        turtle.penup()

while((guess != word)and(errors<10)):
    print('Here,The Word',guess)
    letter = input('Guess a letter')
    hasletter = False
    newguess = []

    for n in range(5):
        if(letter == word[n]):
            newguess.append(letter)
            hasletter = True

        else:
            newguess.append(guess[n])

    guess = ''.join(newguess)
    if (hasletter == True):
        print('Goooood Guess')
    else:
        print('Wrong Guess')
        errors = errors+1
        showStickman()
print('The Word Was',word)
