# Hello Pizza Shop
from myUtils import *

print("Welcome to Pete's Uhh Emporium")

sizeChoice = []
toppingChoice = []
price = 0.00

while True:
    # Choose a size
    sizeOptions = [("Small", 2.00), ("Medium", 3.00), ("Large", 5.00), ("X-Large", 8.00)]
    userEntry = choice("Size", sizeOptions)
    sizeChoice.append(userEntry)
    price += sizeOptions[userEntry][1]

    # Choose a topping
    toppingOptions = [("Meatlovers", 0.00), ("Hawaiian", 0.00), ("Triple Cheese and Bacon", 1.00)]
    userEntry = choice("Topping", toppingOptions)
    toppingChoice.append(userEntry)
    price += toppingOptions[userEntry][1]

    while True:
        another = input("Would you like another pizza? y/n: ").lower()
        if another == "n" or another == "y":
            break
        else:
            continue
    if another == "y":
        continue
    else:
        break


drinkChoice = []
while True:
    # Choose a drink
    drinkOptions = [("No Drink", 0.00),
                    ("Coca Cola", 2.50),
                    ("Fanta", 2.50),
                    ("Sprite", 2.50),
                    ("Bundaberg Ginger Beer", 3.50)
                    ]
    userEntry = choice("Drink", drinkOptions)
    drinkChoice.append(userEntry)
    price += drinkOptions[userEntry][1]

    if input("Would you like another drink? y/n: ").lower() == "y":
        continue
    else:
        break

sideChoice = []
while True:
    # Choose a side
    sideOptions = [("No Side", 0.00),
                   ("Garlic Bread", 2.00),
                   ("Hot Fudge", 4.00),
                   ("Churros", 3.00),
                   ("Mini Dutch Pancakes", 4.00)]
    userEntry = choice("Side", sideOptions)
    sideChoice.append(userEntry)
    price += sideOptions[userEntry][1]

    if input("Would you like another side? y/n: ").lower() == "y":
        continue
    else:
        break


print("You have ordered:")

for choice in sizeChoice:
    print(sizeOptions[sizeChoice[sizeChoice.index(choice)]][0],
          toppingOptions[toppingChoice[sizeChoice.index(choice)]][0])

for choice in drinkChoice:
    print(drinkOptions[drinkChoice[drinkChoice.index(choice)]][0])

for choice in sideChoice:
    print(sideOptions[sideChoice[sideChoice.index(choice)]][0])

print("For a total of ${:.2f}".format(price))