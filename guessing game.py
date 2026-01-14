#import the random method that creates random numbers.
import random

#choosing a number between 1 and 50.
number = random.randint(1,50)
#enter your name.
name = input("state your name:")
#guess is set to false until the player enters the right number.
guess = False
#track the number of tries.
Tries = 0

while guess != number:
    guess = int(input("choose the correct number:"))
    
    if guess < number:
        print("yikes, thats the wrong number. try again")
        Tries = Tries + 1
        
    elif guess > number:
        print("woahh that's way too high. try again")
        Tries = Tries + 1
        
    else:
        print(name,"congrats you got the right number")
        print("your tries:",Tries)
