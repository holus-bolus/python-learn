# typecasting = the process of converting the data type of a value to another data type
# There are two types of typecasting
# 1. Implicit Typecasting
# 2. Explicit Typecasting

name = "Oleksii"
age = 32
gpa = 3.5
is_student = True

# Implicit Typecasting

gpa = int(gpa)

#age = float(age)
age = str(age)
age += "1"
print(age)
my_name = ""
print(bool(my_name))