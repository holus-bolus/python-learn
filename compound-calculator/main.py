principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 1:
        print("Principle amount cannot be less than 1")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 1:
        print("Rate of interest cannot be less than 1")
    else:
        break

while True:
    time = float(input("Enter the time period: "))
    if time < 1:
        print("Time period cannot be less than 1")
    else:
        break

total = principle * (1 + rate / 100) ** time

print(f"The total amount after {time} years is ${total:.2f}")