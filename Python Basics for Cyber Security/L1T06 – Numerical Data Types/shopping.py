"""
A module that takes in product names and prices and displays
the total sum and average of the products
"""
# Get three product names from the user
product_1 = input("Enter a name for product 1: ")
product_2 = input("Enter a name for product 2: ")
product_3 = input("Enter a name for product 3: ")

# Get three product prices from the user
price_1 = int(input("Enter a price for product 1: "))
price_2 = int(input("Enter a price for product 2:"))
price_3 = int(input("Enter a price for product 3:"))

# Calculate the sum of all three products
products_sum = price_1 + price_2 + price_3

# Calculate the average of the products
products_average = round(products_sum / 3, 2)

# Display output to the user
print(f"The Total of {product_1}, {product_2}, {product_3} is \
R{products_sum} and the average price of the items is R{products_average}")
