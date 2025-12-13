student_mark = int(input("Enter the mark of student :- "))
if(student_mark >= 50):

    if(student_mark >= 90):
        print(f"You passed the exam and You got Grade A")
    elif(student_mark >= 80 and student_mark <= 89):
        print(f"You passed the exam and You got Grade B")
    elif(student_mark >= 70 and student_mark <= 79):
        print(f"You passed the exam and You got Grade C")
    else:
        print(f"You passed the exam and You got Grade D")

else:
    print("You are fail due to mark less than 50.")