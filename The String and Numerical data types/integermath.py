''' Create a new Python file called integermath.py.
● Ask the user to enter three different integers.
● Then print out:

○ The sum of all the numbers
○ The first number minus the second number
○ The third number multiplied by the first number
○ The sum of all three numbers divided by the third number
'''

# Ask the user for three integers
num1 = int(input("Please enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))

# Calculations
addition = num1 + num2 + num3

# Outputs
print("Sum of all numbers:", addition)
print("First minus second:", num1 - num2)
print("Third multiplied by first:", num3 * num1)
print("Sum divided by third:", addition / num3)