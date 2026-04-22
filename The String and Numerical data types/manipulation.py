# 1. ask the user to enter a sentence using the input() method.
# Save the user’s response in a variable called str_manip.
# 2. Calculate and display the length of str_manip.
# 3. Find the last letter in str_manip sentence. Replace every occurrence
# of this letter in str_manip with ‘@’.
# 4. Print the last 3 characters in str_manip backwards.
# 5. Create a five-letter word that is made up of the first three characters
# and the last two characters in str_manip.

# 1. input() method
str_manip = input("Enter any sentence: ")

# 2. length of str_manip
print(len(str_manip))

# 3. replace last letter with '@'
last_letter = str_manip[-1]
new_sentence = str_manip.replace(last_letter, "@")
print(new_sentence)

#
print(str_manip[:-4:-1])

# create a five-letter word
first_three = str_manip[0:3]
last_two = str_manip[-2:]
print(first_three + last_two)