# List of questions
# Store the answers
# Randomly pick questions
# Ask the questions
# See if they are correct 
# Keep the track of the score
# Tell the user their score

import random

questions = {
    "What is the keyword to define a function in Python?" : ["def"],
    "Which data type is used to store True or False values?" : ["boolean", "bool"],
    "What is the correct file extension for Python files?" : [".py", "py"],
    "Which symbol is used to write a comment in Python?" : ["#"],
    "Which keyword starts a loop that iterates over a sequence?" : ["for"],
    "What is the keyword to exit a loop in Python?" : ["break"],
    "What is the output of 2 ** 3 in Python?" : ["8"],
}

def python_trivia_game():
    question_list = list(questions.keys())
    total_questions = len(questions)
    score = 0
    
    select_questions = random.sample(question_list, total_questions)
    
    for idx,question in enumerate(select_questions):  # enumerate(...) hands you two things on every loop: a number (the position) and the item itself.
        user_answer = input("Your answer : ").lower().strip()   # User input -> "   PyThON " == "python"
        
        correct_answer = questions[question] # Python goes to the questions dictionary, finds that question, and gives back its value.
        # questions is a dictionary, which stores data as pairs: a key and its value
        # question is the key, and the value is a list of correct answers. It is used as the key to look up the matching answer
       
        if user_answer in correct_answer:
            print("Correct😊 \n")
            score += 1
        else:
            print(f"Incorrect🙃. The correct answer is : {correct_answer} \n")
    
    print(f"Game Over! Your final score is {score} out of {total_questions}.")                

if __name__ == "__main__":            
    python_trivia_game()    