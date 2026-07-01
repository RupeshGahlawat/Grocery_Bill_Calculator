# 🛒 Grocery Bill Calculator

A simple Python console application that calculates the total grocery bill based on selected items and quantities.

##  Features

- Store item names and prices using tuples
- User-friendly console interface
- Input validation using `try-except`
- Calculates total bill
- Applies **20% discount** on bills above ₹150
- Displays the final bill neatly

---

## Available Items

| Item | Price (per kg) |
|------|---------------:|
| Potato | ₹100 |
| Onion | ₹50 |
| Chilli | ₹30 |

---

## Requirements

- Python 3.x

No external libraries are required.

---


##  Sample Output

```
========================================
            GROCERY BILL
========================================
Available Items

Potato  --> ₹100 per kg
Onion   --> ₹50 per kg
Chilli  --> ₹30 per kg
========================================

Enter number of items: 2

Item 1
Enter item name : potato
Enter quantity (kg): 2

Item 2
Enter item name : onion
Enter quantity (kg): 1

========================================
             FINAL BILL
========================================
Item Amounts : (200.0, 50.0)
Subtotal     : ₹250.0
Discount     : 20%
Saved        : ₹50.0
----------------------------------------
Total Amount : ₹200.0
========================================
Thank You for Shopping!
```

---

 Concepts Used

- Tuples
- Lists
- Loops
- Conditional Statements
- Functions (optional)
- Exception Handling (`try-except`)
- Operators

---
