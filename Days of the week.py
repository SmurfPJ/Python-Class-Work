day = input("What day of the week is it: ")
days_forward = int(input("How many days forward: "))

match day:
    case "Mon":
        day_num = 1
    case "Tue":
        day_num = 2
    case "Wed":
        day_num = 3
    case "Thu":
        day_num = 4
    case "Fri":
        day_num = 5
    case "Sat":
        day_num = 6
    case "Sun":
        day_num = 7

final_day = day_num

for new_day in range(days_forward):
    final_day += 1
    if final_day > 7:
        final_day = 1

match final_day:
    case 1:
        print("The new day will be Monday")

    case 2:
        print("The new day will be Tuseday")
        
    case 3:
        print("The new day will be Wednesday")
        
    case 4:
        print("The new day will be Thursday")
        
    case 5:
        print("The new day will be Friday")
        
    case 6:
        print("The new day will be Saturday")
        
    case 7:
        print("The new day will be Sunday")