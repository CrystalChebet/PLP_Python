#week 3 assignment

"""Create a function named calculate_discount(price, discount_percent) 
that calculates the final price after applying a discount. 
The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
If the discount is 20% or higher, apply the discount; otherwise, return the original price.

Using the calculate_discount function, 
prompt the user to enter the original price of an item and the discount percentage. 
Print the final price after applying the discount, or if no discount was applied, print the original price."""

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price

# Get user input and convert to float
price = float(input("Please enter the original price of the item: "))
discount_percent = float(input("Please enter the discount rate for the item (%): "))

# Calculate and print the final price
final_price = calculate_discount(price, discount_percent)
print(f"The final price is: {final_price}")
