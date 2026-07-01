
#     GROCERY BILL


# Tuples
items = ("potato", "onion", "chilli")
prices = (100, 50, 30)

allprice = []

print("=" * 40)
print("        GROCERY BILL")
print("=" * 40)
print("Available Items\n")
print("Potato  --> ₹100 per kg")
print("Onion   --> ₹50 per kg")
print("Chilli  --> ₹30 per kg")
print("=" * 40)

# Number of items
while True:
    try:
        num = int(input("Enter number of items: "))

        if num <= 0:
            print("Please enter a positive number.\n")
            continue

        break

    except ValueError:
        print("Invalid input! Enter a number.\n")

# Input items
for i in range(num):

    print("\n------------------------")
    print("Item", i + 1)
    print("------------------------")

    name = input("Enter item name : ").lower()

    try:
        quantity = float(input("Enter quantity (kg): "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

    except ValueError:
        print("Invalid quantity!")
        continue

    if name == items[0]:
        price = quantity * prices[0]
        allprice.append(price)

    elif name == items[1]:
        price = quantity * prices[1]
        allprice.append(price)

    elif name == items[2]:
        price = quantity * prices[2]
        allprice.append(price)

    else:
        print("Item is out of stock!")

# Convert list into tuple
bill_tuple = tuple(allprice)

# Total bill
bill = sum(allprice)

print("\n" + "=" * 40)
print("           FINAL BILL")
print("=" * 40)

print("Item Amounts :", bill_tuple)
print("Subtotal     : ₹", bill)

if bill >= 150:
    discount = bill * 20 / 100
    bill = bill - discount
    print("Discount     : 20%")
    print("Saved        : ₹", discount)
else:
    print("Discount     : Not Applied")
    print("Spend ₹", 150 - bill, "more to get 20% discount.")

print("-" * 40)
print("Total Amount : ₹", round(bill, 2))
print("=" * 40)
print("Thank You for Shopping!")