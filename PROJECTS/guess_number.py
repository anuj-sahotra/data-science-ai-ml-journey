import random

#Generate a random number
number = random.randint(1,100)
count = 0

while True:
    count += 1
    try:
        guess = int(input("Guess the number between 1 to 100 : "))
        if guess > number:
            print("Choose Smaller number.")
        elif guess < number:
            print("Choose greater number.")
        else:
            print(f"Number matched in {count} attempts.")
            break
        
    except ValueError:
            print("Enter Valid Number.")
        