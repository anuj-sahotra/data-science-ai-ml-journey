import numpy as np

# Rows : Student -> S1, S2, S3, S4, S5
# Columns : Subject -> Maths, Physics, Chemistry

STUDENTS = ["Aman", "Rohit", "Sakshi", "Riya", "Anjali"]
SUBJECTS = ["Maths", "Physics", "Chemistry"]

student_marks = np.array([
    [85, 76, 90],  # Aman
    [70, 98, 100], # Rohit
    [100, 98, 99], # Sakshi
    [33, 45, 48],  # Riya
    [87, 86, 45]   # Anjali
    ])
MAX_TOTAL = student_marks.shape[1] * 100  # 3 subjects, each max 100 marks

def get_grade(percent):
    """Returns grade based on percentage."""
    if percent >= 90:
        return "A"
    elif percent >= 80:
        return "B"
    elif percent >= 70:
        return "C"
    elif percent >= 60:
        return "D"
    else:
        return "F"

# axis=1 means “go across each row,” giving one result per student.
# axis=0 means “go down each column,” giving one result per subject.

def total_marks():
    """Print the total marks of each student."""
    
    totals = student_marks.sum(axis = 1) # total of each student
    
    for idx, marks in enumerate(totals): # enumerate(totals) solves this by handing you pairs of (position, value)
        print(f"{STUDENTS[idx]} total marks is : {marks}/{MAX_TOTAL}")
    
def average_marks():
    """Print the average marks of each student."""
    
    averages = student_marks.mean(axis=1) # average of each student
    
    for idx, avg in enumerate(averages):  
        grade = get_grade(avg)
        print(f"{STUDENTS[idx]} average : {avg:.2f} -> Grade {grade}")
 
def ranking():
    """Print the ranking of students based on total marks."""
    
    totals = np.sum(student_marks, axis=1)       # total of each student
    order = np.argsort(totals)[::-1]             # indices, highest -> lowest
    
    for rank, idx in enumerate(order, start=1):
        print(f"Rank {rank}: {STUDENTS[idx]} -> {totals[idx]}/{MAX_TOTAL}")

def subject_average():
    """Print the average marks of each subject."""
    
    averages = np.mean(student_marks, axis=0)  # average of each subject
    
    for subject, avg in zip(SUBJECTS, averages): # pairs subject names with averages
        print(f"{subject} average marks is : {avg:.2f}")
        
def subject_toppers():
    """Print the top scorer in each subject."""
    
    top_indices = np.argmax(student_marks, axis=0) # argmax -> returns the position of the largest value
    
    for col, subject in enumerate(SUBJECTS):
        top_student = STUDENTS[top_indices[col]]
        top_score = student_marks[top_indices[col], col]
        print(f"{subject} topper: {top_student} ({top_score})")
             
def main():
    """Main function to display menu and call appropriate functions based on user input."""
    
    print("1. Total marks")
    print("2. Average marks")
    print("3. Ranking")
    print("4. Subject average")
    print("5. Subject toppers")
    
    user_input = input("What do you want to get?: ").strip()

    if user_input == "1":
        total_marks()
    elif user_input == "2":
        average_marks()
    elif user_input == "3":
        ranking()
    elif user_input == "4":
        subject_average()
    elif user_input == "5":
        subject_toppers()
    else:
        print("Invalid choice. Enter 1, 2, 3, 4 or 5.")
       
if __name__ == "__main__":
    main()          