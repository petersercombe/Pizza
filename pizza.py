# Hello Pizza Shop
from myUtils import *

print("Welcome to Pete's Uhh Emporium")

# Choose a size
sizeOptions = ["Small", "Medium", "Large", "X-Large"]
sizeChoice = choice("Size", sizeOptions)

# Choose a topping
toppingOptions = ["Meatlovers", "Hawaiian", "Triple Cheese and Bacon"]
toppingChoice = choice("Topping", toppingOptions)

# Choose a drink
drinkOptions = ["Coca Cola", "Fanta", "Bundaberg Ginger Beer", "No Drink"]
drinkChoice = choice("Drink", drinkOptions)

# Choose a side
sideOptions = ["Garlic Bread", "Hot Fudge", "Churros", "Mini Dutch Pancakes"]
sideChoice = choice("Side", sideOptions)

print("You have ordered:")
print(sizeOptions[sizeChoice], toppingOptions[toppingChoice])
print(drinkOptions[drinkChoice])
print(sideOptions[sideChoice])
