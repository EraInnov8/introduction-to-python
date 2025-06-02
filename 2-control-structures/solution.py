# 1. Write a program to find wether given number is divisible by 2

num = int(input("Enter a number."))
if num % 2 == 0:
    print(f"{num} is divisible by 2")
else:
    print(f"{num} is not divisible by 2")


# ------------------------------------------------------------------------------------------------------------------------------------------


# 2. Print ticket prices based on the age of the customer. If a child is between ages 0-12 - print "$5". Teenagers between ages 13-17 - print "$8", Adults between ages 18-64 print "$12" and Seniors between ages 65 and above print "$7".
age = int(input("Enter your age: "))
match age:
    case age if age < 0:
        print("Invalid age")
    case age if 0 <= age <= 12:
        print("$5")
    case age if 13 <= age <= 17:
        print("$8")
    case age if 18 <= age <= 64:
        print("$12")
    case _:
        print("$7")
