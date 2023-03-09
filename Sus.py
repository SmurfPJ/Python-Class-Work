surname = input("Please enter your surname: ")
gender = input("Please enter your gender (m/f/o): ")
age = int(input("Please enter your age: "))
votes = 0

if surname == "ZZZ":
    votes += 1
    if  gender == "m":
        if 30 <= age <= 37:
            votes += 1
    elif gender == "f":
        if 50 <= age <= 60:
            votes += 1

match votes:
    case 0:
        print("not sus")

    case 1:
        print("Kinda Sus")

    case 2:
        print("HUGE SUS")