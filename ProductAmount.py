ht = float(input("Enter the ht: "))
c = input("Enter the category (a, B, c): ").upper()  # Convert the category to uppercase

ttc = 0  # Initialize ttc

if c == 'A':
    ttc = ht + ht * 7 / 100
elif c == 'B':
    ttc = ht + ht * 20 / 100
elif c == 'C':
    ttc = ht + ht * 25 / 100
else:
    print("Invalid category")
