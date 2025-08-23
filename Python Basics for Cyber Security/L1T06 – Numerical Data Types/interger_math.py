"""
A module that takes user input and performs various operations
on the user input
"""

# Obtain user input for calculations
integer1 = int(input("Please enter your first integer: "))
integer2 = int(input("Please enter your second integer: "))
integer3 = int(input("Please enter your third integer: "))

# Perform calculations 
total_sum = integer1 + integer2 + integer3
first_minus_second = integer1 - integer2
sum_divided_by_third = total_sum / integer3

# Display outputs to the user
print(f"The sum of all the integers is {total_sum}")
print(f"The first integer minus the second integer equals \
{first_minus_second}")
print(f"The sum of all three integers divided by the third \
integer is {round(sum_divided_by_third), 2}")
