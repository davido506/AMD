#rock paper scissors
# import PyInputPlus as p
import random

def rock_paper_scissors():
    k = 0
    c = 0

    for i in range(3):

        x = input('Enter your value: ')

        y = random.choice(['rock','paper','scissor'])
        print(y)
        if x == y:
            pass
        if x == 'rock' and y == 'scissor':
            c += 1

        elif x == 'scissor' and y == 'rock':

            k += 1
        elif x == 'paper' and y== 'scissor':

            k += 1
        elif x == 'scissor' and y == 'paper':
            c+=1

        elif x == 'paper' and y== 'scissor':

            k+=1
    if c > k:
        print(f'You won {c}')
    elif c==k:
        print(f'Equal,{k},{c}')
    else:
        print(f'Try again.\nComputer won with {k} points.')




print(rock_paper_scissors())


































