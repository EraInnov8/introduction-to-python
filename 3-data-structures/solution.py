# 1.  Create a dictionary with your personal information (name, age, location, favorite color) and print each key-value pair.
personal_info = {
    "name": "John",
    "age": 50,
    "location": "Berlin",
    "favorite_color": "Blue"
}

for key, value in personal_info.items():
    print(f"{key}: {value}")


# 2.  Write a program that converts temperatures from Celsius to Fahrenheit and vice versa using the formula F = (C * 9/5) + 32.
print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter your choice (1/2): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid choice")
