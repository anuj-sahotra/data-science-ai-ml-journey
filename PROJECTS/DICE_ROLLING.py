"""LOOP:
Ask : Roll the dice
If user enter y - Generate a random numbers - print them.
If user enters n - print thank you message - Terminate
Else - Print invalid choice
"""
import random
while True:
    choice = input("Roll the dice? (y/n) : ").lower()
    if choice == "y":
        dice = random.randint(1,6) # It chooses random number from 1 to 6
        print(dice)

    elif choice == "n":
        print("Thank You.")
        break
    else:
        print("Invalid choice!")    