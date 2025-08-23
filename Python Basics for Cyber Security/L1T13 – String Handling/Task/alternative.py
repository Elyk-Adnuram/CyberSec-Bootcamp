"""Program to convert alternate characters to uppercase or lowercase"""

# Prompt the user for input
user_phrase = input("Please enter a phrase: ")
i = 0
amended_phrase = ""
# Iterate user input and target every 2nd character using i variable
for char in user_phrase:
    i += 1
    if i % 2 == 0:
        amended_phrase += char.lower()
    else:
        amended_phrase += char.upper()  
print("\nDisplay each alternative character in lowercase and uppercase")  
print(amended_phrase)

# Converting each alternative word, split input to list
user_input_list = user_phrase.split()
j = 0
updated_phrase = []
# Iterate user input list and target every 2nd word using j variable
for word in user_input_list:
    j += 1
    if j % 2 == 0:
        updated_phrase.append(word.upper())
    else:
        updated_phrase.append(word.lower()) 
print("\nDisplay each alternative word in lowercase and uppercase") 
print(" ".join(updated_phrase))
