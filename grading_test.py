#! python3

get_grade = int(input("Please enter in a number to convert it to a letter grade: "))

def convert_grade():
    A = range(90,101)
    B = range(80, 90)
    C = range(70, 80)
    D = range(60, 70)
    F = range(50, 60)

    if get_grade in A:


if get_grade < 60:
    if get_grade >= 50 and get_grade < 55:
        get_grade = "-"
        print(f"You got a F{get_grade}")
    else:
        get_grade = "+"
        print(f"You got a F{get_grade}")
elif get_grade >= 60 and get_grade < 70:
    if get_grade >= 60 and get_grade < 65:
        get_grade = "-"
        print(f"You got a D{get_grade}")
    else:
        get_grade = "+"
        print(f"You got a D{get_grade}")
elif get_grade >= 70 and get_grade < 80:
    if get_grade >= 70 and get_grade < 75:
        get_grade = "-"
        print(f"You got a C{get_grade}")
    else:
        get_grade = "+"
        print(f"You got a C{get_grade}")
elif get_grade >= 80 and get_grade < 90:
    if get_grade >= 80 and get_grade < 85:
        get_grade = "-"
        print(f"You got a B{get_grade}")
    else:
        get_grade = "+"
        print(f"You got a B{get_grade}")
elif get_grade >= 90 and get_grade <= 100:
    if get_grade >= 90 and get_grade <95:
        get_grade = "-"
        print(f"You got a A{get_grade}")
    else:
        get_grade = "+"
        print(f"You got a A{get_grade}")
