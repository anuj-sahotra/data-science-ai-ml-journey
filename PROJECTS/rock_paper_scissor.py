import random

Rock = 'r'
Paper = 'p'
Scissor = 's'

emojis = {Rock : "💎", Scissor : "'✂", Paper : "📄"}
choices = tuple(emojis.keys())
def get_user_choice():
    while True:
        user_input = input("Rock, Paper, Scissor? (r/p/s) : ").lower().strip()
        if user_input in choices:
            return user_input
        else:
            print("Invalid choice")
 
def display_choices(user_input, computer):
    print(f"Your Choice : {emojis[user_input]}")
    print(f"Computer Choice : {emojis[computer]}")    
        
def determine_winner(user_input, computer):
    if user_input == computer:
        print("Tie")
    elif(
        (user_input == Rock and computer == Scissor) or 
        (user_input == Scissor and computer == Paper) or 
        (user_input == Paper and computer == Rock)):
        print("YOU WIN!!!")      
    else:
        print("Computer Win!!!")
        
def play_game():
    while True:
        user_input = get_user_choice()                
        computer = random.choice(choices)
            
        display_choices(user_input, computer)
     
        determine_winner(user_input, computer) 

         
                    
        should_continue = input("Continue? (y/n) : ").lower().strip()
        if should_continue != "y":
            break
                
play_game()        