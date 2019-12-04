# Allows for easy packaging of mod materials into the global.json file
# To use, follow the standard operating precedures detailed in the repo

# Imports
import os
import json
from subprocess import Popen
import generalUtilities as gu

# Globals
CATEGORY_NAME = "VARIOUS | SNC Requisitions"
BACKUP_EXT = ".BAK"
GLOBAL_DIR = "../../data/global.json"
# GLOBAL_JSON = {}
MODS_AVAILABLE = []
MODS_SELECTED = []

# Main Thread
def main():
    # Mark globals
    global MODS_AVAILABLE
    global GLOBAL_DIR
    global BACKUP_EXT

    # Check if a global json backup already exists
    backupGlobalJson()

    # Populate the avalible mods list
    for fileName in os.listdir("../"):
        if os.path.basename(os.getcwd()) != fileName and os.path.isdir("../"+fileName):
            MODS_AVAILABLE.append(fileName)

    # Show the main menu
    mainOptions = ["Select Mods", "Pack Mods", "Pack and Start", "Options"]
    gu.textMenu("Brigador Mod Packer", mainOptions, "Quit", mainMenuOptions)

# Menu Triggers
# Triggers for the main menu's options
def mainMenuOptions(choice):
    # Decide what action to take
    if choice == "0":
        modSelectMenu()
    elif choice == "1":
        packageMods()
    elif choice == "2":
        print("Feature TBD")
    elif choice == "3":
        print("Feature TBD")

# Triggers for the mod selection menu's options
def modSelectionOptions(choice):
    # Mark globals
    global MODS_AVAILABLE
    global MODS_SELECTED

    # Make sure the choice is within bounds
    choiceInt = int(choice)
    if choiceInt > 0 and choiceInt <= (len(MODS_AVAILABLE)-2):
        # Mark the chosen mod as a select mod
        MODS_SELECTED.append(MODS_AVAILABLE[choiceInt])

# Functions
# Makes a backup of the global json file if one does not exist yet
def backupGlobalJson():
    # Check if a global json backup already exists
    if not os.path.isfile(GLOBAL_DIR+BACKUP_EXT):
        # Open the read and write global json files
        with open(GLOBAL_DIR, "r", encoding = "Latin-1") as readFile:
            with open(GLOBAL_DIR+".BAK", "w", encoding = "Latin-1") as writeFile:
                writeFile.write(readFile.read())

        # Report that a backup has been made
        print("Made a backup of the global.json file.")

# Populates and opens the mod selection menu
def modSelectMenu():
    # Mark globals
    global MODS_AVAILABLE
    global MODS_SELECTED

    # Create the mod choice list
    modDisplay = {}
    for mod in MODS_AVAILABLE:
        # Check if currently selected
        if mod in MODS_SELECTED:
            modDisplay[mod] = True
        else:
            modDisplay[mod] = False

    # Show mod selection menu until exit
    gu.checkboxMenu("Mod Selection", modDisplay, "Confirm Selections", modSelectionOptions)

    # Print the success message
    print("\n"+str(len(MODS_SELECTED))+" mods have been selected.")

# Packages the selected mods into the global.json file
def packageMods():
    # Mark globals
    global GLOBAL_DIR

    # Look for a global json file
    globalJson = ""
    if os.path.isfile(GLOBAL_DIR):
        # Check if a global json backup already exists
        backupGlobalJson()
            
        # Open the backup global json file
        globalFile = open(GLOBAL_DIR+BACKUP_EXT, "r", encoding="latin-1")

        # Assign the data to the global json
        globalJson = json.load(globalFile, encoding="latin-1")

        # Close the backup global json file
        globalFile.close()
    else:
        # Tell the user no file exists
        print("Somehow you don't have a global.json file. You should fix that ASAP.")
        exit()
    
    print(globalJson)

# Begin Operation
if __name__ == '__main__':
    main()