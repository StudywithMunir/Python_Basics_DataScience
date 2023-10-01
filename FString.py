# Example 1: Basic f-string
name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

# Output: Hello, my name is Alice and I am 30 years old.

# Example 2: Using f-string with expressions
radius = 5
area = f"The area of the circle with radius {radius} is {3.14 * radius ** 2}."
print(area)

# Output: The area of the circle with radius 5 is 78.5.

# Example 3: f-string with formatted output
pi = 3.14159265359
formatted_pi = f"Value of pi (rounded to 2 decimal places): {pi:.2f}"
print(formatted_pi)

# Output: Value of pi (rounded to 2 decimal places): 3.14
