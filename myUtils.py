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

def choice(category, list):
    print(f'{category} options: ')
    prompt = 'Enter the number of your ' + category.lower() + ' choice (e.g. "2"): '
    listLooper(list)
    return inputNumber(prompt, list)
