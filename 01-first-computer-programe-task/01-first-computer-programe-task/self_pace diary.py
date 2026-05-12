'''  As i am learning python i am writing a diary to keep track of
my progress and thoughts. This is a small project that i will be working on to
practice my python skills and also to document my learning journey.
I will be writing about what i have learned, what i am struggling with,
and what i am looking forward to learning next. I hope that this diary will
help me stay motivated and focused on my learning goals.I have just learned
variable so this is a simple
diary entry to practice using variables in python. I will be using variables
to store my thoughts and feelings about my learning journey. I will also be
using variables to keep track of my progress and to set goals for myself.
I am excited to see how this diary will evolve as i continue to learn and grow
as a python programmer.
'''

# Prompt user username and store it in a variable
username = input("Please enter your name: ")
age = input("Please enter your age: ")
what_learned = input("What have you learned today?: ")
struggle = input("What are you struggling with today?: ")
date = input("What is today's date ?: ")
time = input("What time is it now ?: ")
thoughts = input("What are your thoughts about what you learned today?:")
project = input('''Do you want to improve past project or start
                new one? Y or N: ''').lower()
if project == "y":
    project_name = input("What is the name of the project you want to improve?: ")
    print(f"You have chosen to improve the project: {project_name}")
elif project == "n":
    new_project_name = input("What is the name of the new project you want to start?: ")
    print(f"You have chosen to start a new project: {new_project_name}")
else:
    print("Invalid input. Please enter Y or N.")

# Print out the diary entry
print(f"Diary Entry for {date} at {time}")
print(f"Username: {username}")
print(f"Age: {age}")
print(f"What I learned today: {what_learned}")
print(f"What I am struggling with today: {struggle}")
print(f"My thoughts about what I learned today: {thoughts}")
print(f"Project choice: {project}")
print("Thank you for writing! Keep up the good work and keep learning")

# add a file to write the documented diary entry
with open("diary_entry.txt", "w") as file:
    file.write(f"Diary Entry for {date} at {time}\n")
    file.write(f"Username: {username}\n")
    file.write(f"Age: {age}\n")
    file.write(f"What I learned today: {what_learned}\n")
    file.write(f"What I am struggling with today: {struggle}\n")
    file.write(f"My thoughts about what I learned today: {thoughts}\n")
    file.write(f"Project choice: {project}\n")
    file.write("Thank you for writing! Keep up the good work and keep learning\n")