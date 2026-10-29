import random

emojis = {"r" : "💎", "s" : "'✂", "p" : "📄"}
choices = ["r", "p", "s"]

while True:
    user_input = input("Rock, Paper, Scissor? (r/p/s) : ").lower().strip()
            
    if user_input not in ("r" ,"p",  "s"):
        print("Invalid choice")
        continue
                
    computer = random.choice(choices)
            
    print(f"Your Choice : {emojis[user_input]}")
    print(f"Computer Choice : {emojis[computer]}")    
            
    if user_input == computer:
        print("Tie")
    elif(
        (user_input == "r" and computer == "s") or 
        (user_input == "s" and computer == "p") or 
        (user_input == "p" and computer == "r")):
        print("YOU WIN!!!")      
    else:
        print("Computer Win!!!")
                
    should_continue = input("Continue? (y/n) : ").lower().strip()
    if should_continue != "y":
        break
                
        