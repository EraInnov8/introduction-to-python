# Data Types

# int
age = 25
print(age)
print(type(age))


# float
price = 19.99
print(price)
print(type(price))


# complex
complex_number = 2 + 3j
print(complex_number)
print(type(complex_number))

print("Real part:", complex_number.real)
print("Imaginary part:", complex_number.imag)


# str
greeting = "Hello World"
print(greeting)

# characters
first_char = greeting[0]
print("First character:", first_char)

# slicing
hello_part = greeting[:5]
print("Sliced string:", hello_part)

# string reverse
str_reverse = greeting[:-1]
print(str_reverse)


# bytes, bytearray
byte_data = b'Hello'
print(byte_data)

# byte element
first_byte = byte_data[0]
print("ASCII code for letter 'H'", first_byte)

# Bytearray
byte_array_data = bytearray(b'World')
print(byte_array_data)

# Modifying a byte
byte_array_data[0] = ord('w')
print("Modified bytearray:", byte_array_data)


# bool
is_true = 100 > 101
print(is_true)

is_false = 'H' == 'h'
print(is_false)

print(type(is_true))
print(type(is_false))


# Note - You can convert data types in Python using functions like int(), float(), str(), and others.

# -------------------------------------------------------------------------

# Data Structures

# List
shopping_list = ["milk", "eggs", "bread"]
print(shopping_list)

# Adding an item
shopping_list.append("cheese")
print(shopping_list)

# Accessing an item
print(shopping_list[0])

# Modifying an item
shopping_list[1] = "brown eggs"
print(shopping_list)


# Tuples
rgb_color = (255, 0, 0)  # Red color in RGB
print(rgb_color)
print(rgb_color[0])

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)


# Dictionaries
address_book = {"John": "123 Main St", "Jane": "456 Elm St"}
print(address_book)

# Accessing a value
print(address_book["John"])

# Adding a new entry
address_book["James"] = "789 Oak St"
print(address_book)


# Sets
unique_visitors = set()
visitor_ids = ["user1", "user2", "user1", "user3"]

unique_visitors = visitor_ids

print(unique_visitors)


# ---------------------ASSIGNMENT---------------------
# 1.  Create a dictionary with your personal information (name, age, location, favorite color) and print each key-value pair.
# Refer - https://www.freecodecamp.org/news/python-dictionary-methods-dictionaries-in-python/
# Hint - read about items()

# 2.  Write a program that converts temperatures from Celsius to Fahrenheit and vice versa using the formula F = (C * 9/5) + 32.
