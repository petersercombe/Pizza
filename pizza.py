# Hello Pizza Shop


def listLooper(list):
    for option in list:
        print(list.index(option), "-", option)

def inputNumber(prompt, list):
    try:
        userInput = int(input(prompt))
    except ValueError:
        print("Please enter a valid number")
        # continue
    else:
        return userInput


print("Welcome to Pete's Uhh Emporium")

# Choose a size
sizeOptions = ["Small", "Medium", "Large", "X-Large"]
print("Size options: ")
listLooper(sizeOptions) # Calls our listLooper function for the sizeOptions list
sizeChoice = inputNumber("Enter your size choice: ", sizeOptions)

# Choose a topping
toppingOptions = ["Meatlovers", "Hawaiian", "Triple Cheese and Bacon"]
print ("Topping options: ")
listLooper(toppingOptions)
toppingChoice = input("Enter your topping choice: ")
