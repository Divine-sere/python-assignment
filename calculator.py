price = float(input("Enter your price: "))
discount = float(input("Enter the discount percentage: "))

if discount >= 0:
    final_price = price - (price * discount / 100)
else:
    final_price = price

print(f"Final price: ${final_price:.2f}")
