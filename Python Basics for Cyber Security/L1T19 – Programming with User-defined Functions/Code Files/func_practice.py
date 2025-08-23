#   Inside it, create a function called 'add_three', that takes as input three
#   different parameters num1, num2, num3.
#   Next, write logic to create a new variable, called y,
#   that is the sum of all three of these numbers.
#   Then, return the result y.
#   Now, after you've defined this function, write a function call to return
#   the sum of the numbers 52, 25, and 1403.
#   Store this result in a variable called sum_func.
#   Print out sum_func. Don't forget to cast to a string!


def add_three(num1, num2, num3):
    y = num1 + num2 + num3
    return y


sum_func = add_three(52, 25, 1403)

print(f"The sum of the values are {sum_func}")

