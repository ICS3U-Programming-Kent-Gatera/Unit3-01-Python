#!/usr/bin/env python3
# Created By: Kent Gatera
# Date: 10.3.22
# Tax is calculated using price from user input.


# The HST tax in British Columbia is 5%.
HST = 0.05

# get input of total price.
total_price = float(input("What is the price of your item? : " + "$"))

tax = HST * total_price
float(tax)
print("{:.2f}".format(tax))
total_cost = total_price + tax
# Add the total price and tax for the total cost.
print(
    "The total price is ${0:.2f} + ${1:.2f} = ${2:.2f}".format(
        total_price, tax, total_cost
    )
)
