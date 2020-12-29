'''
Created on 23 dec. 2020

@author: Caroline
'''
import random
import math
a = 1
b = 250
x = random.randint(a,b)
guess_x = math.inf
turn = 0

def multiple(x, guess_x):
    ans = x * guess_x
    print(str(int(ans)) + "\n")

def divisible(x, guess_x):
    ans = x / guess_x
    print(str(int(ans)) + "\n")

def minus(x, guess_x):
    ans = x - guess_x
    print(str(int(ans)) + "\n")
    
def plus(x, guess_x):
    ans = x + guess_x
    print(str(int(ans)) + "\n")

def unvalid():
    print("This isn't a valid number!")  
     
while guess_x != x and turn < 5:
    try:
        guess_x = int(input("Please give a number between " + str(a) + " and " + str(b) + "\n"))
    except:
        unvalid()
    else:
        if guess_x < a or guess_x > b:
            unvalid()
        else:
            turn += 1
            if guess_x != x :
                print("Hint: ")
                hint = random.choice([multiple, divisible, minus, plus])
                hint(x, guess_x)
if guess_x == x:
    print("\nYou won in "+ str(turn) + " turn(s)!")
else:
    print("You used "+ str(turn) + " turns, but you didn't guess the number. It was " + str(x) + "!")
