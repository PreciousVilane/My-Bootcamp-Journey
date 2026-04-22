# 1. Reprint this sentence as “The quick brown fox jumps over the lazy dog.”
# using the replace() function to replace every “!” exclamation mark with a
# blank space.

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
New_sentence = sentence.replace("!", " ")
print(New_sentence)


# 2. Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER THE LAZY
# DOG.” using the upper() function

capital_sentence = New_sentence.upper()
print(capital_sentence)

# 3. Print the sentence in reverse.
print(New_sentence[::-1])