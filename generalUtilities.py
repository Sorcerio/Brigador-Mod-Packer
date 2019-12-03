# General Utilities v1.0 for Python by Brody Childs
# Allows ease of use though providing generalized methods for commonly used Python code blocks.

# Configuration
TITLE_MARKER_LEFT = "["
TITLE_MARKER_RIGHT = "]"

# Methods
# Ask the user to input a valid answer and returns the choice once answered.
# query -> String to ask the user. Has ": " appened to its end
# validAnswers -> List of answer strings that are valid
# showChoices -> If the choices provided should be shown to the user by this function
def askUser(query, validAnswers, showChoices = True):
    # Build options string
    answers = str(validAnswers[0])
    for i in range(1, len(validAnswers)):
        answers += (", "+str(validAnswers[i]))
    
    # Show Options if applicable
    if showChoices:
        print("Choose one: "+answers)
    
    # Set to lowercase valid answers
    validAnswers = [str(answer).lower() for answer in validAnswers]

    # Enter query loop
    answer = None
    while answer == None or answer.lower() not in validAnswers:
        # Ask user for input
        answer = input(query+": ")

    # Return answer
    return answer

# Asks the user a yes or no question.
# query -> String to ask the user. Has ": " appened to its end
# boolean -> If the return value should be a boolean as opposed to a string
def askUserYesNo(query, boolean = False):
    # Check what mode
    if boolean:
        # Ask user
        answer = askUser(query, ["Yes","No"])

        # Check answer
        if answer.lower() == "yes":
            return True
        else:
            return False
    else:
        # Run standard questioning
        return askUser(query, ["Yes","No"])

# Prints and retains a menu system based on provided information leaving the calling program to decide function.
# title -> The title of the menu
# choices -> List of choice titles for the menu
def presentTextMenu(title, choices):
    # Print title
    print(TITLE_MARKER_LEFT+" "+title+" "+TITLE_MARKER_RIGHT)

    # Print Menu
    index = 0
    numberList = []
    for choice in choices:
        # Print choice
        print("["+str(index)+"] "+choice)

        # Add choice to number list
        numberList.append(index)

        # Iterate
        index += 1

    # Print instructions
    print("Select a number to choose the option.")
    
    # Ask user for choice and return
    return askUser("Choice", numberList, False)

# Asks for user input while watching for an exit phrase that if entered returns a 'None' object.
# query -> Question to ask the user for input on. Has ": " appended to it
# exitPhrase -> String to listen for to indicate no response
def managedInput(query, exitPhrase):
    # Display query
    print("Enter '"+str(exitPhrase)+"' to "+(str(exitPhrase).lower())+".")

    # Ask user for input
    answer = input(query+": ")

    # Check if exit phrase
    if answer.lower() == exitPhrase.lower():
        # Send exit tag
        return None
    else:
        # Send inputted answer
        return answer

# Asks for user input of a number while watching for an exit phrase that if entered.
# Returns a 'None' object if canceled.
# query -> Question to ask the user for input on. Has ": " appended to it
# exitPhrase -> String to listen for to indicate no response
def managedInputNumber(query, exitPhrase):
    # Enter validation loop
    answer = None
    goodNumber = False
    while not goodNumber:
        # Get managed input
        answer = managedInput(query, exitPhrase)

        # Check if valid
        if answer != None:
            # Attempt to convert to int
            try:
                # Convert to number
                answer = int(answer)

                # Exit loop
                goodNumber = True
                break
            except ValueError as err:
                # Tell user to fix it
                print("'"+str(answer)+"' is not a number.")
        else:
            # Canceled, break loop
            break

    # Check final verdict
    if goodNumber:
        return answer
    else:
        return None

# Asks for user input of a number while watching for an exit phrase that if entered.
# Returns a 'None' object if canceled.
# query -> Question to ask the user for input on. Has ": " appended to it
# maxNumber -> The maximum number that would be considered valid (inclusive)
# minNumber -> The minimum number that would be considered valid (inclusive)
# exitPhrase -> String to listen for to indicate no response
def managedInputNumberRange(query, maxNumber, minNumber, exitPhrase):
    # Enter validation loop
    answer = None
    withinRange = False
    while not withinRange:
        # Get input
        answer = managedInputNumber(query, exitPhrase)

        # Check if valid
        if answer != None:
            # Check if within range
            if answer <= maxNumber and answer >= minNumber:
                # Within range
                withinRange = True
        else:
            # Canceled, break loop
            break
    
    # Final check
    if withinRange:
        return answer
    else:
        return None

# Prints a text menu and handles input between an accompanied execution function all within a handled loop.
# title -> The title of the menu
# choices -> List of choice titles for the menu
# lastOption -> Option to add to the last of the choices. Often 'Back' or 'Quit'
# func -> The function to call within the script that calls this function that uses the data gathered from this function
def textMenu(title, choices, lastOption, func):
    # Prep answer choice
    answer = None

    # Add last option to choices
    choices.append(lastOption)

    # Enter main loop
    while answer == None or answer != str(len(choices)-1):
        # Present main menu and wait for input
        print("")
        answer = presentTextMenu(title, choices)

        # Apply answer to main menu functions
        func(answer)

# Example of the method the 'textMenu()' function is looking for in the 'func' parameter.
# This can be used as a template and for learning to understand the process of the 'textMenu()' function.
def exampleTextMenuFunction(answer):
    # Print the returned answer
    print("textMenu: "+str(answer))

# Prints a text menu and handles input between an accompanied execution function all within a handled loop.
# title -> The title of the menu
# choices -> List of choice titles for the menu
# lastOption -> Option to add to the last of the choices. Often 'Back' or 'Quit'
# func -> The function to call within the script that calls this function that uses the data gathered from this function
# package -> Data that is sent along with whatever choice is made to be used later
def textMenuWithPackage(title, choices, lastOption, func, package):
    # Prep answer choice
    answer = None

    # Add last option to choices
    choices.append(lastOption)

    # Enter main loop
    while answer == None or answer != str(len(choices)-1):
        # Present main menu and wait for input
        print("")
        answer = presentTextMenu(title, choices)

        # Apply answer to main menu functions
        func(answer,package)

# Example of the method the 'textMenuWithPackage()' function is looking for in the 'func' parameter.
# This can be used as a template and for learning to understand the process of the 'textMenuWithPackage()' function.
def exampleTextMenuWithPackageFunction(answer, package):
    # Print the returned answer
    print("textMenu w/ package: "+str(answer)+" w/ "+str(package))

# Reads the entire contents of a file to memory and returns the content as a lumpsum string (good for JSON files, etc).
# fileName -> Name (or full address path if not in the working directory) of the file to read
def readFullFile(fileName):
    # Open the file
    with open(fileName, "r") as rFile:
        # Read and return the data
        return rFile.read()

# Writes the entire contents of the supplied text to the specified tile (good for JSON files, etc).
# fileName -> Name (or full address path if not in the working directory) of the file to write to. Be sure to include the file extension
# text -> The text to write to the file in one pass (can include new line, tab, etc characters)
def writeFullFile(fileName, text):
    # Open the file
    with open(fileName, "w") as wFile:
        # Write the text out
        wFile.write(text)
