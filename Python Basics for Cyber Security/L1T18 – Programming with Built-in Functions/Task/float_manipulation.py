"""Get user input as floats and perform mathematical operations on the input"""

import statistics

floats = []

# Obtain ten floats from the user and append to floats list
while True:
    user_input = round(float(input("Please enter a float: ")))
    floats.append(user_input)
    if len(floats) == 10:
        print("Thanks for the numbers.")
        break

# Perform mathematical operations on the floats list
total = sum(floats)
max_number = max(floats)
min_number = min(floats)
mean_number = round(statistics.mean(floats), 2)
median_number = round(statistics.median(floats), 2)

# Display above variables to the user
print(f"The total of the numbers are: {total}")
print(f"The index of the maximum number is: {floats.index(max_number)}")
print(f"The index of the minimum number is: {floats.index(min_number)}")
print(f"The average of the numbers entered is: {mean_number}")
print(f"The median number is: {median_number}")
