# Hello Pizza Shop
from myUtils import *

print("Welcome to Pete's Uhh Emporium")

sizeChoice = []
toppingChoice = []

while True:
    # Choose a size
    sizeOptions = ["Small", "Medium", "Large", "X-Large"]
    sizeChoice.append(choice("Size", sizeOptions))

    # Choose a topping
    toppingOptions = ["Meatlovers", "Hawaiian", "Triple Cheese and Bacon"]
    toppingChoice.append(choice("Topping", toppingOptions))

    if input("Would you like another pizza? y/n: ").lower() == "y":
        continue
    else:
        break


drinkChoice = []
while True:
    # Choose a drink
    drinkOptions = ["No Drink", "Coca Cola", "Fanta", "Bundaberg Ginger Beer"]
    drinkChoice.append(choice("Drink", drinkOptions))

    if input("Would you like another drink? y/n: ").lower() == "y":
        continue
    else:
        break


# Choose a side
sideOptions = ["No Side", "Garlic Bread", "Hot Fudge", "Churros", "Mini Dutch Pancakes"]
sideChoice = choice("Side", sideOptions)


print("You have ordered:")

for choice in sizeChoice:
    print(sizeOptions[sizeChoice[sizeChoice.index(choice)]],
          toppingOptions[toppingChoice[sizeChoice.index(choice)]])

for choice in drinkChoice:
    print(drinkOptions[drinkChoice[drinkChoice.index(choice)]])

print(sideOptions[sideChoice])
