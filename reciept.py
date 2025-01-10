import math
import datetime as dt

username = "MountainDev"
first_name = "Isaiah"
middle_init = "D."
last_name = "Nevin"
date_of_purchase = dt.datetime.now()

full_name = first_name + " " + middle_init + " " + last_name

quantity = 3;
unit_price = 2000;
sales_tax_rate = 0.065
subtotal = unit_price * quantity;
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax


output=f"""
name:          {full_name}
date of puchase:   {date_of_purchase}

subtotal:     ${quantity * unit_price:>9,.2f}
sales tax     ${sales_tax:>9,.2f}
total         ${total:>9,.2f}
"""

print(output)
