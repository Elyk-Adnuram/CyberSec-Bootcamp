# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error 
# messages, and find and fix the errors.

# Syntax error: Parentheses missing in print statements 
print("Welcome to the error program")
print("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
# Syntax error: Equality operator used instead of assignment operator 
age_Str = "24 years old"
# Runtime error: trying to cast a string with non-numeric characters to int 
# Fixed by making age variable an integer
age = 24
# Syntax error: cannot use addition operator with string and int data type 
# Used f-string for variable interpolation 
print(f"I'm {age} years old.")

# Variables declaring additional years and printing the total years of age
years_from_now = "3"
# Runtime error: trying to add string and in
# Casting 'years_from_now' to int to avoid type error 
total_years = age + int(years_from_now)

# Syntax error: Parentheses missing in print statements 
print("The total number of years:" + "answer_years")

# Variable to calculate the total number of months from the given number of 
# years and printing the result
# Syntax error: 'total' is not defined, should be 'total_years' 
# Logical error: 6 months not included in the calculation 
# Fixed by adding 6 months to the total years 
total_months = total_years * 12 + 6
# Syntax error: Parentheses missing in print statements 
# Used f-string for variable interpolation 
print(f"In 3 years and 6 months, I'll be {total_months}  months old")

# HINT, 330 months is the correct answer
