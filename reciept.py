
import datetime as dt

# user inputs
first_name = input("Please input your first name: ")
middle_init = input("Please input your middle initial: ")
last_name = input("Please input your last name: ")

# Capture the current date and time
date_of_purchase = dt.datetime.now()

# round to the nearest minute
if date_of_purchase.second >= 30:
    date_of_purchase += dt.timedelta(minutes=1)
date_of_purchase = date_of_purchase.replace(second=0, microsecond=0)

# format the rounded date and time
date_of_purchase_str = date_of_purchase.strftime("%Y-%m-%d %H:%M")

# format full name
full_name = first_name + " " + middle_init + " " + last_name

# numbers for calculation
quantity = 3;
unit_price = 2000;
sales_tax_rate = 0.065

# calculations
subtotal = unit_price * quantity;
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax


# Output formatting
output=f"""
name:              {full_name}
date of puchase:   {date_of_purchase}

quantity:      {quantity:>9,.2f}
unit price:   ${unit_price:>9,.2f}
subtotal:     ${quantity * unit_price:>9,.2f}
sales tax:    ${sales_tax:>9,.2f}

total:        ${total:>9,.2f}

Thank you for you purchase!
"""

# Print the receipt
print(output)
