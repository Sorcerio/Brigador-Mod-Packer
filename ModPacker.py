# Allows for easy packaging of mod materials into the global.json file
# To use, follow the standard operating precedures detailed in the repo

# Imports
import os
import json
from subprocess import Popen
import generalUtilities as gu

# Globals
CATEGORY_NAME = "VARIOUS | SNC Requisitions"
GLOBAL_JSON = {}
SELECTED_MODS = []

# Main Thread
def main():
    # Show the main menu
    mainOptions = ["Select Mods", "Pack Mods", "Pack and Start", "Options"]
    gu.textMenu("Brigador Mod Packer", mainOptions, "Quit", mainMenuOptions)

# Triggers for the main menu's options
def mainMenuOptions(choice):
    # Decide what action to take
    if choice == "0":
        print("Feature TBD")
    elif choice == "1":
        print("Feature TBD")
    elif choice == "2":
        print("Feature TBD")
    elif choice == "3":
        print("Feature TBD")

# Begin Operation
if __name__ == '__main__':
    main()