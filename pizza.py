# Hello Pizza Shop


def listLooper(list):
    for option in list:
        print(list.index(option), "-", option)

def inputNumber(prompt, list):
    while True:
        try:
            userInput = int(input(prompt))
        except ValueError:
            print("Please enter a valid number")
            continue
        else:
            if userInput < len(list) and userInput >= 0:
                return userInput
            else:
                print("Choice entered is outside the range of options. Please try again.")
                continue


print("Welcome to Pete's Uhh Emporium")

# Choose a size
sizeOptions = ["Small", "Medium", "Large", "X-Large"]
print("Size options: ")
listLooper(sizeOptions) # Calls our listLooper function for the sizeOptions list
sizeChoice = inputNumber("Enter the number of your size choice (e.g. '2'): ", sizeOptions)

# Choose a topping
toppingOptions = ["Meatlovers", "Hawaiian", "Triple Cheese and Bacon"]
print ("Topping options: ")
listLooper(toppingOptions)
toppingChoice = inputNumber("Enter the number of your topping choice: ", toppingOptions)



print("You have ordered a", sizeOptions[sizeChoice], toppingOptions[toppingChoice])
