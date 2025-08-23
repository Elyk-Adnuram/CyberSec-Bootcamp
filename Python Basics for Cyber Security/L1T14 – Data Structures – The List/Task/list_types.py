"""Access elements of lists and display them to the user"""

friends_names = ['Jenny Jones', 'Willem Visagie', 'David Radebe']

# Display name of first friend, last friend and length of the list
print(f"First friend: {friends_names[0]}\nLast friend: {friends_names[-1]}\n\
Length of the list: {len(friends_names)}\n")

friends_ages = [28, 39, 45]

for index, name in enumerate(friends_names):
    # Access each age using the index
    age = friends_ages[index]
    print(f"{name} is {age} years old.")
