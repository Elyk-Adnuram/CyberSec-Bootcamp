"""
A program to calculate the total cost of a user's 
holiday based on the inputs received from the user
"""
cities_flight_costs = {
    "cape town": 1100,
    "johannesburg": 1070,
    "durban": 700
}

# Obtain user inputs for the flight, car and hotel fees
while True:
    city_flight = input("Select a city: Cape Town, Johannesburg, \
or Durban: ").strip().lower()
    if city_flight == "cape town" or city_flight == "johannesburg" or\
city_flight == "durban":
        break
    
num_nights = int(input("Enter the number of nights you will be staying at the \
hotel: "))
rental_days = int(input("Enter the number of days you will be hiring a car \
for: "))


def hotel_cost(nights):
    """
    Calculate The cost for hotel stay

    Parameters:
    nights (int): Number of nights for hotel stay

    Returns:
    int: The cost for the hotel stay
    """
    return nights * 850


def plane_cost(flight):
    """
    Calculate the flight cost for each city

    Parameters:
    flight (str) : The city chosen by the user

    Returns:
    int: The cost of the flight to the specified city
    """
    if flight == "cape town":
        return cities_flight_costs[flight]
    elif flight == "johannesburg":
        return cities_flight_costs[flight]
    elif flight == "durban":
        return cities_flight_costs[flight]
    else:
        return 0
    

def car_rental(days):
    """
    Calculate the car rental costs

    Parameters:
    days (int): The number of days the car will be rented for

    Returns:
    int: The cost of the car rental
    """
    return days * 350


def holiday_cost(hotel, plane, car):
    """
    Calculate the total cost of the holiday

    Parameters:
    hotel (int) : The cost for the hotel stay
    plane (int) : The cost for the flight
    car (int) : The cost for the car rental

    Returns:
    int : Total cost for the holiday
    """
    return hotel_cost(hotel) + plane_cost(plane) + car_rental(car)


# Store the values returned from the functions to variables
hotel_fees = hotel_cost(num_nights)
flight_fees = plane_cost(city_flight)
vehicle_rental = car_rental(rental_days)
total_holiday_cost = holiday_cost(num_nights, city_flight, rental_days)

# Display the costs to the user
print(f"The cost for the hotel stay will be R{hotel_fees}")
print(f"The cost for the flight will be R{flight_fees}")
print(f"The cost for the vehicle rental will be R{vehicle_rental}")
print(f"The total cost for the holiday will be R{total_holiday_cost}")
