# Day 9 of 100 for the Udemy Python Bootcamp
# Exercise 9-1: Grading

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    if student_scores[student] >= 90:
        student_scores[student] = "Outstanding"
        student_grades[student] = student_scores[student]
    elif student_scores[student] >=80:
        student_scores[student] = "Exceeds Expectations"
        student_grades[student] = student_scores[student]
    elif student_scores[student] >= 70:
        student_scores[student] = "Acceptable"
        student_grades[student] = student_scores[student]
    elif student_scores[student] <= 70:
        student_scores[student] = "FAILED"
        student_grades[student] = student_scores[student]
    # Debugging
    #print(student_scores[student])

# 🚨 Don't change the code below 👇
print(student_grades)

# 91 - 100 = "outstanding"
# 81 - 90 = "exceeds expectations"
# 71 - 80 = "acceptable"
# < 70 = "failed"