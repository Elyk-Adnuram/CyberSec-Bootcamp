"""Module to display star pattern in a single for loop"""

stars = ""
# Stars for loop which iterates 9 times for the length of pattern
for i in range(1, 10):
    if i < 5:
        stars = "*" * i
        print(stars)
    # Print decreasing star pattern
    else:
        stars = "*" * (10 - i)
        print(stars)


star = "*"  # variable stores character used in pattern
pattern = ""  # variable will store each line of pattern
count = 5  # the variable will be used to count down from 5 in if statement

for i in range(1, 10):  #loop will run 9 times, it starts counting from 1 not 0
    if i > 5:  # check if current value in loop is greater than 5
        count = count - 1  # counter is reduced by 1 on every loop
        print(pattern[:count]) # pattern with 5 stars is sliced to count value and displayed
    else:  # runs when i is less or equal to 5
        pattern += star  # concatenate the string star   
        print(pattern)  # displays pattern


