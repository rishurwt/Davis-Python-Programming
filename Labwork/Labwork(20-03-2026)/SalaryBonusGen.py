def calculate_bonus(salary, years):
    if years >= 10:
        bonus_percent = 20
    elif years >= 5:
        bonus_percent = 10
    else:
        bonus_percent = 5
    bonus_amount = (salary * bonus_percent) / 100
    return bonus_amount, bonus_percent
for i in range(1, 4):
    print(f"\n--- Employee {i} ---")
    sal = float(input("Enter Salary : "))
    exp = float(input("Enter Experience (years) : "))
    amount, percent = calculate_bonus(sal, exp)
    
    print(f"Bonus percent: {percent}%")
    print(f" Bonus Amount : {amount}")
    print(f"Total Salary (Salary + Bonus): {sal + amount}")