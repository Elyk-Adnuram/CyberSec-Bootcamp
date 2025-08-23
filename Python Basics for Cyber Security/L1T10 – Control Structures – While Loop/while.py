"""This script calculates the average of the user input"""

# Save user inputs to this list
numbers = []

# Ask user for input and cast it to a float inside of a while loop
while True:
    user_number = float(input("Enter a number or -1 to stop program: "))
    numbers.append(user_number)
# Once condition is met, end loop and calculate average
    if user_number == -1:
        numbers.pop()
        if len(numbers) > 0:
            average = sum(numbers) / len(numbers)
            break

        print("Please enter at least one number")

print(f"The average of the numbers entered excluding the -1 is {average}")
