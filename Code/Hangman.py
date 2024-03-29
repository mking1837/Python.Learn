import random

wordlist = ['grape', 'melon', 'chair', 'table', 'brush', 'pasta', 'shirt', 'pants', 'shoes', 'socks', 'watch', 'phone', 'mouse', 'paper', 'books', 'apple', 'mango', 'peach', 'lemon', 'berry', 'onion', 'radis', 'beets', 'beans', 'steak', 'pizza', 'bread', 'train', 'plane', 'boats', 'bikes', 'jeeps', 'sedan', 'coupe', 'wagon', 'truck', 'David', 'James', 'Henry', 'Sarah', 'Alice', 'piano', 'clock']
word = random.choice(wordlist)
guess =  '*****'

while(guess != word):
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
print('The Word Was',word)
