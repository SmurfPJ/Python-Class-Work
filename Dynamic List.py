names = []

num = input("How many names do you want to input: ")
num = int(num)

for i in range(0, num):
    user_name = input("Enter the name: ")
    names.append(user_name)

print(names)