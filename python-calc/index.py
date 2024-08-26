first_number = int(input('Enter the first number  '))
second_number = int(input('Enter the second number  '
                          ))
operator = input('Enter the operator: =,-,* or /  ');

if operator == '+':
    print(f"{first_number + second_number}")
elif operator == '-':
    print(f"{first_number - second_number}")