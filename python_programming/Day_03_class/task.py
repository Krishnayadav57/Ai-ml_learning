# write a program to calculate the total
#  bill to be paid of several units of items after deducting discount and adding tax

units = int(input("Enter the number of unit :- "))
price = float(input("enter the price of per unit :- "))

total = units * price
       # discount is 20%

discount = 0.20
discount_amount = discount * total

# tax rate = 13%
tax = 0.13
tax_amt = 0.13 * (total - discount_amount)

final_amt = total - (discount_amount + tax_amt)

print (f" Actual Amount to be paid is :- {final_amt}")


