''' mastering the building blocks for
    more complex code
    by writing a simple age quiz that asks the user for their age
    and responds with a message based on the input.
'''


# Get user input and convert to integer
age = int(input("Enter your age: "))

# Check conditions in the correct order
if age > 100:
    print("Sorry, you're dead.")
elif age == 21:
    print("Congrats on your 21st!")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")