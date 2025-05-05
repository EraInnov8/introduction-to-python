# Conditional Statements

# Keyword - if else
# Program to write eligibility of voters
age = 21
if age >= 18:
    print('You are eligible to vote. Please vote.')
else:
    print('You are still young. Come back when you are 18.')

# Keyword - elif
# Program to find grade of a student
score = int(input("Enter your score: "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# ----------------------------------------------------------

# Loops
# Keyword - for
fruits = ["apple", "banana", "cherry"]
for berry in fruits:
    print(berry)


# Keyword - while
# Printing natural numbers from 1 to 5
num = 1
while num <= 5:
    print(num)
    num = num+1

# ----------------------------------------------------------

# Jump Statements

# Keyword - break
foods = ["apple", "banana", "cherry", "date"]
target = "cherry"
for food in foods:
    print(f"Checking if {food} is {target}...")
    if food == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found in the list")


# Keyword - continue
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


# Keyword - return
def add_numbers(a, b):
    result = a + b
    return result


num1 = 5
num2 = 7
result = add_numbers(num1, num2)
print(f"Result is {result}")


# Keyword - pass
# null operation is used as a placeholder when a statement is required syntactically, but no execution of code is necessary.
a = 0
if a == 5:
    pass
else:
    pass

# ----------------------------------------------------------


# Loops and conditional statements
# Is the number entered by user greater than or less than or equal to 0
for __ in range(3):
    n = int(input('Enter a number '))
    if n > 0:
        print('Greater than 0')
    elif n < 0:
        print('Lesser than 0')
    else:
        print('You entered 0 ')


# ---------------------ASSIGNMENT---------------------

# 1. Write a program to find wether given number is divisible by 2.
# 2. Print ticket prices based on the age of the customer. If a child is between ages 0-12 - print "$5". Teenagers between ages 13-17 - print "$8", Adults between ages 18-64 print "$12" and Seniors between ages 65 and above print "$7".
