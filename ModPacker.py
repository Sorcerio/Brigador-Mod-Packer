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
GLOBAL_JSON = {}
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
    global MODS_SELECTED

    # Look for a global json file
    if os.path.isfile(GLOBAL_DIR):
        # Check if a global json backup already exists
        backupGlobalJson()

        # Open the backup global json file
        globalFile = open(GLOBAL_DIR+BACKUP_EXT, "r", encoding="latin-1")

        # Assign the data to the global json
        GLOBAL_JSON = json.load(globalFile, encoding="latin-1")

        # Close the backup global json file
        globalFile.close()
    else:
        # Tell the user no file exists
        print("Somehow you don't have a global.json file. You should fix that ASAP.")
        exit()

    # Collect the json files from the selected mods
    modPaths = []
    for mod in MODS_SELECTED:
        # Loop through the files in each mod folder
        for dirpath, dirnames, filenames in os.walk("../"+mod):
            # Loop through the files in the current directory
            for filename in filenames:
                # Make sure it's a valid json
                if filename != "global.json" and os.fsdecode(filename).endswith(".json"):
                    # Formulate the full file path
                    path = (dirpath+"/"+filename).replace("\\", "/").replace("//", "/")

                    # Add the build path to the mod paths
                    modPaths.append(path)

    print(modPaths)

# Adds the given json mod to global
# Currently Supports: All Vehicles, All Weapons, Pilots, Specials
def addModToGlobal(data, path):
    # Watch out for archetype failures
    try:
        # Check if the data is a Mech
        if data['archetype'] == "MECH":
            # Look for mod packer entry
            hasCategory = False
            categoryIndex = -1
            tick = 0
            for item in GLOBAL_JSON['mechs']:
                if item['name'] == CATEGORY_NAME:
                    hasCategory = True
                    categoryIndex = tick-1
                    break

                # Iterate
                tick += 1
            
            # Add category if needed
            if not hasCategory:
                # Get index that will be added
                categoryIndex = len(GLOBAL_JSON['mechs'])

                # Add to category
                GLOBAL_JSON['mechs'].append({'name' : CATEGORY_NAME, 'list' : []})

            # Add Mod link to category
            for category in GLOBAL_JSON['mechs']:
                if category['name'] == CATEGORY_NAME:
                    category['list'].append(pathToStandard(path))
                    break

        # Check if the data is a Pilot
        elif data['archetype'] == "PILOT":
            # Append to Pilots
            GLOBAL_JSON['pilots'].append(pathToStandard(path))

        # Check if the data is a weapon
        elif "_WEAPON" in data['archetype']:
            # Decide category based on title
            if "aux" in path:
                GLOBAL_JSON['aux_weapons'].append(pathToStandard(path))
            elif "main" in path:
                GLOBAL_JSON['main_weapons'].append(pathToStandard(path))
            elif "turret" in path:
                GLOBAL_JSON['turret_weapons'].append(pathToStandard(path))
            elif "heavy" in path:
                GLOBAL_JSON['heavy_weapons'].append(pathToStandard(path))
            elif "small" in path:
                GLOBAL_JSON['small_weapons'].append(pathToStandard(path))
            elif "special" in path:
                GLOBAL_JSON['special_abilities'].append(pathToStandard(path))

        # Check if the data is a mission
        elif "MISSION" in data['archetype']:
            # Append to Missions
            GLOBAL_JSON['missions'].append(pathToStandard(path))

        # Check if the data is an overmap
        elif "OVERMAP" in data['archetype']:
            # Append to Overmap Paths
            GLOBAL_JSON['overmap_paths'].append(pathToStandard(path))

    except KeyError as e:
        print(path+" is not an archetype file, ignoring")

# Converts a local path from the mod packer folder to the Brigador standard
def pathToStandard(path):
    # Replace and send
    return path.replace("../","assets/_modkit/")

# Begin Operation
if __name__ == '__main__':
    main()