#=======================================================================================================================
# TASK 2
#
#=======================================================================================================================

import random as rnd

dice = 0
guess = 0


def getDiceGuess():
    guess = 0

    while guess not in ('1','2','3','4'):
        print('Guess the number on a 4- sided dice! Enter a number between 1 and 4:')
        guess = input()

    return int(guess)

def rollDice():

    dice = rnd.randint(1, 4)
    guess = getDiceGuess()

    if dice == guess:
        print('You are good!')
        return
    else:
        print('Sorry! Try to guess again!')
    guess = getDiceGuess()

    if dice == guess:
        print('Congrats! You got it!')
        return
    else:
        print('Sorry! Your second chance!')
        guess = getDiceGuess()

    if dice == guess:
        print('Congrats! You got it!')
        return
    else:
        print('Sorry! You third can try!')
        guess = getDiceGuess()

    if dice == guess:
        print('Congrats! You got it!')
        return
    else:
        print('Nope. You are really bad at this game.')

rollDice()