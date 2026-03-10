## TASK # 01  (USER INFORMATION)

# asking user to enter full name
full_name = input("Enter your full name: ")
# asking user for favorite color
fav_color = input("Enter your favorite color: ")
# asking user for birth year
birth_year = int(input("Enter your birth year: "))
# calculating age
age = 2026 - birth_year
# printing messages using f-strings
print(f"Welcome, {full_name}!")
print(f"Your favorite color is {fav_color} – perfect for calm AI thinking.")
print(f"You were born in {birth_year} → you are currently {age} years old (2026).")




# TASK # 02 (SIMPLE CALCULATOR)

# taking numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# asking which operation to perform
operator = input("Enter operation (+, -, *, /, **, %): ")
# checking the operation
if operator not in ["+", "-", "*", "/", "**", "%"]:
    print("Invalid operator!")
elif operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result:.2f}")
elif operator == "**":
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result:.2f}")
elif operator == "%":
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")



# Task # 03 (part A)

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
number = start
while number <= end:
# skip numbers divisible by 7
    if number % 7 == 0:
        number += 1
        continue
    if number % 2 == 0 and number % 5 == 0:
        print(f"{number} --> Even & Multiple of 5!!")
    elif number % 2 == 0:
        print(f"{number} -→ Even")
    elif number % 5 == 0:
        print(f"{number} -→ Multiple of 5!")
    else:
        print(number)
    number += 1




# TASK # 03  (part B)
password = input("Enter a password: ")
if len(password) < 6:
    print("Too short!")
elif not any(ch.isdigit() for ch in password):
    print("Add at least one number")
elif not any(ch.isupper() for ch in password):
    print("Add at least one capital letter")
else:
    print("Strong password,  good choice!")