# Create two variables pointing to the same integer
a = 256
b = a

print(f"Address of a: {id(a)}")
print(f"Address of b: {id(b)}")

# Bonus: Change one variable
print("\nChanging variable 'a'...")
a = a + 1

print(f"New address of a: {id(a)}")
print(f"Address of b:     {id(b)}")