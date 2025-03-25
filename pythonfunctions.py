def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    The discount is only applied if it's 20% or higher.
    """
    if discount_percent >= 20:  # Only apply discount if 20% or more
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return original price if discount is less than 20%

# Taking user input for price and discount percentage
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calling the function and printing the result
final_price = calculate_discount(price, discount_percent)

# Displaying the result
if final_price == price:
    print(f"No discount applied. Final price: {final_price:.2f}")
else:
    print(f"Discount applied! Final price after {discount_percent}% off: {final_price:.2f}")
