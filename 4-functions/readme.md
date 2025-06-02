# Functions

## What are they?

A function is a reusable block of code that performs a specific task. For example - in an e-commerce application like Amazon, they may decide to use functions to calculate the total amount at checkout.

## Why do we use functions?

When writing code, developers adhere to the principle of **DRY** - Don't Repeat Yourself. This fundamental concept encourages developers to avoid duplicating code and write reusable functions. By doing so, functions help in maintaining clean, efficient, and maintainable code.

Additionally, functions enable developers to break down complex problems into smaller problems. For example, during a checkout process multiple tasks like processing payment, updating inventory and sending confirmation emails are implemented which are often divided into reusable code. In case an unexpected error arises during checkout, it makes it easier and quick to test and fix isolated pieces of code in functions.6

## Types of functions

1. **Built-in Functions**

   1. `print()`, `input()`, `len()`, `max()`, `min()`
   2. Type conversion functions - `int()`, `float()`, `str()`
   3. Mathematical functions - `abs()`, `round()`, `sum()`

2. **User-defined Functions**

   1. Function definition with `def` keyword.
   2. Function naming conventions: Function names are all lower case and separate by underscore. For example: `calculate_tax()`, `get_user_name()`

3. **Lambda Functions**

These are anonymous functions with lambda syntax. Usually a single expression that returns the result.

## Function Parameters and Arguments

Parameters are variables in function definition.
Arguments are the actual values passed to function.

1. Positional arguments - are arguments where the position and number of parameters matter.
2. Keyword arguments- are arguments where you need to specify parameter name. Here the order of parameter does not matter.
3. Default parameters- are arguments with default values.

## Function Return Values

- Functions use the `return` statement and may have one or multiple returning values. There are functions without return (None) as well.

## Variable-length Arguments

1. `*args` - is a keyword with arbitrary positional arguments that converts into a tuple. It is used when you don't know how many arguments will be passed.
2. `**kwargs` - is a keyword with arbitrary keyword arguments that converts into a dictionary. It is used for optional configuration options.

## Function Scope

Python searches for variables in this order -

1. Local - Inside current function
2. Enclosing - In enclosing function (nested functions)
3. Global - At top level of module
4. Built-in - Pre-defined names

### Additional Resources to refer to -

1. [How to Use \*args and \*\*kwargs in Python](https://www.freecodecamp.org/news/args-and-kwargs-in-python/)
2. [Defining Your Own Python Function](https://realpython.com/defining-your-own-python-function/)
