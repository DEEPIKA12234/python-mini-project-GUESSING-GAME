import random
x=random.randint(1,100)

print("Let's play a game, you have only  5 chances")
attempt=0
while attempt<5:
        y=int(input("come on guess the number between 1 to 100:"))    
        if y<x:
            print(" you need to go higher, guess again")   
        elif y>x:
            print("you need to guess lower, guess again")
        else:
            x==y
            print("Bingoooooo You won")
            break
        print("you have",4-attempt,"chance")
        attempt=attempt+1
if attempt==5:
        print(" you loose, the number was",x)

