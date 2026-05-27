# Electricity Bill Calculator

# 1. Accept Input
name = input("Enter Customer Name: ")
units = float(input("Enter Units Consumed: "))

# 2. Calculate Bill
if units <= 100:
    total_bill = units * 5
else:
    # First 100 units at ₹5, remaining at ₹18
    total_bill = (100 * 5) + ((units - 100) * 18)

# 3. Print Professional Receipt
print("\n" + "="*30)
print(f"{'ELECTRICITY BILL':^30}")
print("="*30)
print(f"Customer Name  : {name}")
print(f"Units Consumed : {units} units")
print("-" * 30)
print(f"TOTAL AMOUNT   : ₹{total_bill:,.2f}")
print("="*30)
print(f"{'Thank You!':^30}")