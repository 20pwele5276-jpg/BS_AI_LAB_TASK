# task #01
def welcome_message():
    print("Welcome to Python Programming Lab ")
welcome_message()

# task#02
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print("The sum is:  " , result)

# task#03
def functionB():
    print("Inside functionB")
    
    
def functionA():
    print("Inside Function A")
    
functionA()
functionB()

# task#04
def greet(name = "student"):
    print("hello", name)
    
greet()
greet("wajiha")

# task#05
x = 10  
def show_scope():
    print("Inside function, x =", x)
    y = 20 
    
show_scope()
print("Outside function, x =", x)

# task#06
def total_numbers(*numbers):
    total = sum(numbers)
    return total

print("total  numbers= ", total_numbers (1,2,34,5))
    
# task#07
def student_info(**data):
    for key, value in data.items():
        print(key , value)

student_info(Name  = " wajiha" , Age = 20, RollNo = "24PWAI0002")
    
# task#08
square = lambda x: x *x

print("square = ", square(10))

# task#09
numbers = [ 1,2,3,4,5]
square = list(map(lambda x: x * x , numbers))

print("squares = ", square)

# task#10
marks = [45, 67, 82, 30, 90, 55]
square = list(map(lambda x: x > 50 , marks))

print("squares = ", square)

# -----------------------------lab tasks end--------------------------

##Task Mini Project: Student Marks Analyzer
print("Task Mini Project: Student Marks Analyzer")

# taking marks from user
marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

# function to calculate total
def total_marks(data):
    return sum(data)

# function to calculate average
def average_marks(data):
    return sum(data) / len(data)

# using lambda to find highest marks
highest = max(marks, key=lambda x: x)

# calling functions
total = total_marks(marks)
average = average_marks(marks)

# displaying results
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Marks:", highest)

#-------------------------------------------------------------

##Mini-Project: "AI Number Guessing Game Lite"
print("Mini-Project: AI Number Guessing Game Lite")

import random   # importing random module to generate number

# computer selects a random number between 1 and 50
secret = random.randint(1, 50)
# total attempts allowed
attempts = 7

# counter to track how many tries used
count = 0

print("Welcome to AI Number Guessing Game Lite!")
print("Guess a number between 1 and 50")


# loop runs until attempts finish
while count < attempts:

    # taking input from user
    guess = int(input("Enter your guess: "))

    # checking if input is in valid range
    if guess < 1 or guess > 50:
        print("Please enter a number between 1 and 50\n")
        continue   # skip rest and ask again

    # increasing attempt count
    count += 1

    # checking conditions
    if guess > secret:
        print("Too high!")

    elif guess < secret:
        print("Too low!")

    else:
        # correct guess
        print(f"You win in {count} attempts!")
        print("AI training level: Beginner → Intermediate")
        break   # exit loop when correct

    # showing remaining attempts
    remaining = attempts - count
    print(f"Attempts left: {remaining}")
    
# if user fails after all attempts
if count == attempts and guess != secret:
    print("Game Over!")
    print(f"The correct number was {secret}")