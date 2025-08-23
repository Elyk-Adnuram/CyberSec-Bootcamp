# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error 
# messages, and find and fix the errors.

# Syntax error: parentheses are missing in the print function #
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16
# Fixing the string formatting to use f-strings for better readability
# Logical error: variables are out of order in the string #
full_spec = f"This is a {animal}. It is a {animal_type} and it has \
{number_of_teeth} teeth"
# Syntax error: parentheses are missing in the print function 
print(full_spec)
