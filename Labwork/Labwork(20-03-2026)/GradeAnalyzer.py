def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
all_marks = [95, 82, 67, 40, 76]
for marks in all_marks:
    grade = calculate_grade(marks)
    print(f"Marks: {marks} -> Grade: {grade}")