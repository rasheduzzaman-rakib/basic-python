#guessing game
a=int(input("Enter the start value: "))
b=int(input("Enter the end value: "))
for x in range(a,b):
    from random import randint
    guessNumber=int(input("Enter your guess between a and b: "))
    randomNumber=randint(a,b)
    if guessNumber==randomNumber:
        print("You have won")
    else:
        print("You have lost")
        print("Random number was",randomNumber)