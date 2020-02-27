'''
Q1. Write a program that asks the user to input a character to 
guess a character from a-z. The user should be allowed five tries for guessing.


#using for loop
print("Enter the Character that you want to be guessed")
c = input()

for x in range(5):
    print("Guess the Character")
    a =  input()
    if a == c:
        print("You Guess the Right word")
        break
    elif x == 4:
        print("Best of luck for next time" )
    else:
        print("Keep Trying. Remaining Tries:" + str(4-x))

'''
#using while loop
import random
import string
# print("Enter the Character that you want to be guessed")
# c = input()
# to get random alphabets
alphabets =  string.ascii_lowercase
random_letter = random.choice(alphabets)

x=0
while x <5:
    print("Guess the Character")
    a =  input()
    x+=1
    if a == random_letter:
        print("You Guess the Right word")
        break
    elif x == 5:
        print("Letter was {}".format(random_letter))
        print("Best of luck for next time" )
    else:
        print("Keep Trying. Remaining Tries:" + str(5-x))


 
