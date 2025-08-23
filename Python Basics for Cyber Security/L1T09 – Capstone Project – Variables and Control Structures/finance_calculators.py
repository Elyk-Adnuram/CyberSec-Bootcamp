"""An investment and home loan repayment calculator"""

import math

# Provide menu for user to choose from
while True:
    calculator_type = input("""
    Investment - to calculate the amount of interest you'll earn on your investment. 
    Bond - to calculate the amount you'll have to pay on a home loan.
    Enter either “investment” or “bond” from the menu above to proceed: """).lower()
    if calculator_type == "bond" or calculator_type == "investment":
        # Calculations based on bond choice
        if calculator_type == "bond":
            bond_amount = int(input("Enter the present value of the house: "))
            bond_int_rate = float(input("Enter the interest rate (only enter\
            the integer e.g. 8 for 8%): "))/100/12
            months = int(input("Enter the number of months over which the \
            bond will be repaid: "))
            monthly_repayment = (bond_int_rate * bond_amount) / \
                (1 - (1 + bond_int_rate) ** (-months))
            print(f"The monthly repayment is {round(monthly_repayment, 2)}")

        # Calculations based on investment choice
        elif calculator_type == "investment":
            deposit_amount = int(input("Enter the deposit amount: "))
            investment_int_rate = float(input("Enter the interest rate (only enter the\
            integer e.g. 8 for 8%): "))/100
            investment_years = int(input("Enter the number of years for your  \
            investment: "))
            interest_type = input("Enter your chosen interest type - simple or \
            compound: ").lower()
            if interest_type == "simple":
                simple_int_investment = deposit_amount * \
                    (1 + investment_int_rate * investment_years)
                print(
                    f"The simple interest amount is {round(simple_int_investment, 2)}")
            elif interest_type == "compound":
                compound_int_investment = deposit_amount * \
                    math.pow((1 + investment_int_rate), investment_years)
                print(
                    f"The simple interest amount is {round(compound_int_investment, 2)}")

        else:
            print("Please choose bond or investment")
