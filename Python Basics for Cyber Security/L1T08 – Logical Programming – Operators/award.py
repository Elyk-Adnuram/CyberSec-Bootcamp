"""Determine the award a user will received based on their triathlon time"""

# Obtain triathlon times from user and save into variables
swim_time_mins = int(input("Enter your swimming time in minutes: "))
cycle_time_mins = int(input("Enter your cycling time in minutes: "))
run_time_mins = int(input("Enter your running time in minutes: "))

# Calculate the total time by adding the other times 
total_time_minutes = swim_time_mins + cycle_time_mins + run_time_mins
print(f"Total time taken for the triathlon: {total_time_minutes} minutes")

# Determine award based on total time of user
if total_time_minutes <= 100:
    print("Award: Provincial colours")
elif total_time_minutes <= 105:
    print("Award: Provincial half colours")
elif total_time_minutes <= 110:
    print("Award: Provincial scroll")
else:
    print("No award")
