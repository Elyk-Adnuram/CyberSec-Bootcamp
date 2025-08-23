"""
This module uses the string manipulation method 'replace' to
print out a variable with all occurrences of a character replaced
and also prints the variable in reverse
"""

# Hero variable with exclamation marks
single_string = "The!quick!brown!fox!jumps!over!the!lazy!dog."
# Using the replace method to replace occurrences of '!'
single_string_replaced = single_string.replace("!", " ")
print(single_string_replaced) 
# Printing the modified string in uppercase
single_string_upper = single_string_replaced.upper()
print(single_string_upper)
# Printing the modified string in reverse
single_string_reversed = single_string_replaced[::-1]
print(single_string_reversed)
