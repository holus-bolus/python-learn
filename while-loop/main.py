# age = int(input("Enter your age: "))
#
# while age < 0:
#     print("Age cannot be negative")
#     age = int(input("Enter your age: "))
#
# print(f"Your age is {age}")

# food = input("Enter your favourite food (q to quit): ")
#
# while food != "q":
#     print(f"Your favourite food is {food}")
#     food = input("Enter your favourite food (q to quit): ")

number = int(input("Enter a number between 1 and 10: "))

while number < 1 or number > 10:
    print("Number is out of range")
    number = int(input("Enter a number between 1 and 10: "))

