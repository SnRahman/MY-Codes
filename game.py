# Paper Rock Scissor Game

import random

print('Choose your choice')
print( '1 -> Rock')
print( '2 -> Paper')
print( '3 -> Scissor')

items= ('','Rock','Paper','Scissor')

player = int(input())
computer = random.randrange(1,3)

print('Player Choose : {}'.format(items[player]))
print('Computer Choose :' + items[computer])

if player == computer:
    print('Match Tied, Try again!')
elif player == 1 and computer == 3:
    print('Congrates You win')
elif player == 2 and computer == 1:
    print('Congrates You win')
elif player == 3 and computer == 2:
    print('Congrates You win')
else:
    print('You Lose, best of luck next time.')

