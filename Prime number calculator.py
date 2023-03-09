import math

number = input('What number would you like to check: ')

if number.isdigit() == True:
    number = int(number)
    if number % 2 == 0:
        print(number, " is Even")
    else:
        print(number, " is Odd")

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(number, " is not a prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
else:
    print("That is not a number")