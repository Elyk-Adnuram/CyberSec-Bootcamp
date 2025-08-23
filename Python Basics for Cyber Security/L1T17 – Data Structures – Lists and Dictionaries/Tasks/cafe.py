"""Calculate the total worth of stock"""

# List of menu items
menu = ['chocolate cake', 'lamingtons', 'milk tart', 'malva pudding']

# Dictionary containing item quantities
stock = {
    'chocolate cake': 26,
    'lamingtons': 40,
    'milk tart': 12,
    'malva pudding': 20
}

# Dictionary containing item prices
stock_prices = {
 'chocolate cake': 190,
 'lamingtons': 8,
 'milk tart': 80,
 'malva pudding': 145
}

total_stock = 0
# iterate menu list using each list item as a key
for item in menu:
    total_stock += stock[item] * stock_prices[item]

print(f"Total stock value is R{total_stock}")
