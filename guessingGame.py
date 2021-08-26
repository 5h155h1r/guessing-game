import random

chances=0
num = random.randint(0,9)
print(num)
print("Guess a number from 1 to 9") 

while(chances<5):
    guess = int(input("Guess: "))
    if(guess>num):
        print("too high")
    elif(guess<num):
        print("too low")
    elif(guess==num):
        print("YOU WIN!")
        break
    chances=chances+1
        
if(chances==5):
    print("You lose, the number was " + str(num))
   

