# input() = a function that allows user to input data and returns it as a string
user_input = input("Enter your name: ")  # this will prompt the user to enter their name
age = int(input("Enter your age: "))  # this will prompt the user to enter their age
age += 1  # this will increment the user's age by 1
print(f"Hello {user_input}")  # this will print the user's name
print("Happy birthday!")  # this will print a birthday message
print(f"You are {age} years old")  # this will print the user's age

length = int(input("Enter the length area: "))
width = int(input("enter the width: "))
print(f"The rectangle area is {length * width}")
