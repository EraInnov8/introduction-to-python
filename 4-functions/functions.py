# Built-in Functions

# print()
print("Hello, World!")

# Type conversion functions
age = "25"
print("Age (string):", age)
age = int(age)
print("Age (integer):", age)

# Mathematical functions
numbers = [1, 2, 3, 4, 5]
print("Sum of numbers ", sum(numbers))
print("Maximum value ", max(numbers))
print("Minimum value ", min(numbers))


# User-defined Functions

def welcome():
    f_name = input('What is your name? ')
    print('Welcome' + ' ' + f_name)


welcome()

# With arguments and return value

# Positional arguments


def calculate_rectangle_area(length, width):
    return length * width


area = calculate_rectangle_area(10, 5)
print(f"Rectangle area is {area}")

# Keyword arguments
area = calculate_rectangle_area(width=8, length=12)  # Order doesn't matter
print(f"Rectangle area (using keywords) is {area}")


# Default parameters
def power(base, exponent=2):
    return base ** exponent


print(f"power(5) = {power(5)}")
print(f"power(5, 3) = {power(5, 3)}")


# Mixing different argument types
# Creating user profile with mixed parameters

def create_profile(name, age, city="Unknown", country="USA"):
    return f"{name}, {age} years old, from {city}, {country}"


print(create_profile("Bob", 25))
print(create_profile("Jef", 30, "New York"))
print(create_profile("Charlie", 28, city="Paris", country="France"))


# Lambda Functions

# Square of a number
def cube(y):
    return y*y*y


def lambda_cube(y): return y*y*y


print("Using function defined with `def` keyword, cube:", cube(5))
print("Using lambda function, cube:", lambda_cube(5))


# Single return value
def square(number):
    """Return the square of a number"""
    return number ** 2


result = square(7)
print(f"Square of 7: {result}")


# Multiple return values
def calculate_stats(numbers):
    return min(numbers), max(numbers), sum(numbers), sum(numbers)/len(numbers)


numbers = [10, 20, 30, 40, 50]
minimum, maximum, total, average = calculate_stats(numbers)
print(f"Stats for {numbers}:")
print(f"Min: {minimum}, Max: {maximum}, Sum: {total}, Avg: {average}")


# Function without return (returns None)
def print_separator(char="-", length=40):
    print(char * length)


result = print_separator("=", 20)
print(f"Return value: {result}")


# Variable-length Arguments

# *args
def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


print("Sum of numbers:", sum_numbers(1, 2, 3, 4, 5))

# **kwargs


def total_fruits(**fruits):
    total = 0
    for num in fruits.values():
        total += num
    return total


print(total_fruits(banana=5, mango=7, apple=8))
print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
print(total_fruits(banana=5, mango=7))


# Combining regular args, *args, and **kwargs
def complete_function(required, *args, **kwargs):
    print(f"Required parameter: {required}")
    print(f"Additional positional args: {args}")
    print(f"Keyword arguments: {kwargs}")


complete_function("mandatory", 1, 2, 3, name="Test", value=100)


# Function Scope
x = 10  # global variable


def my_function():
    x = 20  # local variable
    print("Local x:", x)


my_function()
print("Global x:", x)


# ---------------------ASSIGNMENT---------------------
# 1. Write a program to calculate the total bill for a customer based on the following parameters - prices, and tax rate.
# prices = [10.99, 4.99, 2.99]
# tax_rate = 8
# Print the total bill amount and round it to 2 digits after decimal.

# 2. Write a program to calculate the change due to a customer based on the amount paid and the total cost of the items purchased. It should print the amount due if any. If not, print - Insufficient Payment.
# Case 1 - total_cost = 18.97 and amount_paid = 20.00
# Case 1 - total_cost = 18.97 and amount_paid = 15.00
