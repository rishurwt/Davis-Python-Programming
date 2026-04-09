marks = {"A": 80, "B": 95, "C": 78}
top_student = max(marks, key=marks.get)
print(f"Output: {top_student}")