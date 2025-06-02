# 1. Write a program to calculate the total bill for a customer based on the following parameters - menu items, prices, and tax rate.
def calculate_total_bill(prices, tax_rate):
    total_cost = sum(prices)
    tax = (total_cost * tax_rate) / 100
    total_bill = total_cost + tax
    return total_bill


prices = [10.99, 4.99, 2.99]
tax_rate = 8
total_amount = round(calculate_total_bill(prices, tax_rate), 2)
print('Total amount is ', total_amount)

# ------------------------------------------------------------------------------------------------------------------------------------------

# 2. Write a program to calculate the change due to a customer based on the amount paid and the total cost of the items purchased


def calculate_change_due(amount_paid, total_cost):
    change_due = round(amount_paid - total_cost, 2)
    return change_due


def display_change_due(amount_paid, total_cost):
    change_due = calculate_change_due(amount_paid, total_cost)
    if change_due >= 0:
        print(f"Change Due: ${round(change_due, 2)}")
    else:
        print("Insufficient Payment")


# Case - 1
total_cost = 18.97
amount_paid = 20.00
display_change_due(amount_paid, total_cost)


# Case - 2
total_cost = 18.97
amount_paid = 15.00
display_change_due(amount_paid, total_cost)
