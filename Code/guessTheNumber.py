import random
number = random.randint(1,100)
playerguess = 0
while(number != playerguess):
    playerguess = int(input('Guess The Number'))
    if(playerguess > number):
       print('Too Big')
    if(playerguess < number):
       print('Too Small')
print("Nice Guess, That's Correct")
