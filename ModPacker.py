# Allows for easy packaging of mod materials into the global.json file
# To use, follow the standard operating precedures detailed in the repo

# Imports
import os
import json
import subprocess
import generalUtilities as gu

# Globals
CATEGORY_NAME = "VARIOUS | SNC Requisitions"
BACKUP_EXT = ".BAK"
SETTINGS_FILE = "settings.json"
SETTINGS = None
GLOBAL_DIR = "../../data/global.json"
GLOBAL_JSON = {}
MODS_AVAILABLE = []
MODS_SELECTED = []

# Main Thread
def main():
    # Mark globals
    global MODS_AVAILABLE
    global MODS_SELECTED
    global GLOBAL_DIR
    global BACKUP_EXT
    global SETTINGS_FILE
    global SETTINGS

    # Check if a global json backup already exists
    backupGlobalJson()

    # Load the settings from the file
    with open(SETTINGS_FILE, "r") as sFile:
        SETTINGS = json.load(sFile)

    # Populate the selected mods list
    populateModsFromSettings()

    # Populate the avalible mods list
    for fileName in os.listdir("../"):
        if os.path.basename(os.getcwd()) != fileName and os.path.isdir("../"+fileName):
            MODS_AVAILABLE.append(fileName)

    # Show the main menu
    mainOptions = ["Select Mods", "Play with Selected Mods", "Play without Mods", "Options"]
    gu.textMenu("Brigador Mod Packer", mainOptions, "Quit", mainMenuOptions)

# Menu Triggers
# Triggers for the main menu's options
def mainMenuOptions(choice):
    # Mark globals
    global MODS_SELECTED
    global SETTINGS

    # Decide what action to take
    if choice == "0":
        # Mod selection menu
        modSelectMenu()
    elif choice == "1":
        # Play with selected mods
        # Package the mods
        packageMods()

        # Compile the mods
        compileGlobalJson()

        # Start Brigador
        startBrigador()
    elif choice == "2":
        # Play vanilla
        # Clear the selected mods list
        MODS_SELECTED.clear()

        # Package the mods
        packageMods()

        # Compile the mods
        compileGlobalJson()

        # Start Brigador
        startBrigador()

        # Populate the selected mods list again
        populateModsFromSettings()
    elif choice == "3":
        # Options menu
        print("Feature TBD")

# Triggers for the mod selection menu's options
def modSelectionOptions(choice):
    # Mark globals
    global MODS_AVAILABLE
    global MODS_SELECTED
    global SETTINGS
    global SETTINGS_FILE

    # Make sure the choice is within bounds
    choiceInt = int(choice)
    if choiceInt > 0 and choiceInt <= (len(MODS_AVAILABLE)-2):
        # Pull the mod file
        modFile = MODS_AVAILABLE[choiceInt]

        # Add/Remove the mod to the settings and the selected mod list
        if modFile in SETTINGS['Mods']:
            # Mod is already in the list, remove it
            SETTINGS['Mods'].remove(modFile)
            MODS_SELECTED.remove(modFile)
        else:
            # Mod is not in the list, add it
            SETTINGS['Mods'].append(modFile)
            MODS_SELECTED.append(modFile)

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

    # Save the settings file
    with open(SETTINGS_FILE, "w") as sFile:
        json.dump(SETTINGS, sFile)

    # Print the success message
    print("\n"+str(len(MODS_SELECTED))+" mods have been selected.")

# Packages the selected mods into the global.json file
def packageMods():
    # Mark globals
    global GLOBAL_DIR
    global GLOBAL_JSON
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
    for mod in MODS_SELECTED:
        # Loop through the files in each mod folder
        for dirpath, dirnames, filenames in os.walk("../"+mod):
            # Loop through the files in the current directory
            for filename in filenames:
                # Make sure it's a valid json
                if filename != "global.json" and os.fsdecode(filename).endswith(".json"):
                    # Formulate the full file path
                    path = (dirpath+"/"+filename).replace("\\", "/").replace("//", "/")

                    # Open and load the selected json file
                    with open(path, "r", encoding="latin-1") as jsonFile:
                        try:
                            # Attempt to parse the json data
                            jsonData = json.load(jsonFile)
                        except Exception:
                            # Inform the user that the json file isn't valid
                            print(path+" is not a valid .json file.")
                        else:
                            # If the file was parsed, add mod to the global json
                            addModToGlobal(jsonData, path)

    # Open the global json file to write to
    globalJsonFile = open(GLOBAL_DIR, "w", encoding="latin-1")

    # Dump the new global data to the global json
    json.dump(GLOBAL_JSON, globalJsonFile)

    # Close the global json file
    globalJsonFile.close()

# Adds the given json mod to global
# Currently Supports: All Vehicles, All Weapons, Pilots, Specials
def addModToGlobal(data, path):
    # Mark globals
    global CATEGORY_NAME
    global GLOBAL_JSON

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

# Compiles the current global json file so the mods it contains can be used in game
def compileGlobalJson():
    # Report that the compiler will open
    print("\nOpening the compiler. Please wait for it to complete, this may take a while.")

    # Trigger the compiler process
    subprocess.call(["../../../brigador.exe", "-genpack"], cwd=r"../../../")

    # Report that hte compiler has closed
    print("\nCompiler has finished.")

# Starts the Brigador game
def startBrigador():
    # Mark globals
    global MODS_SELECTED
    global SETTINGS

    # Mark that the game is opening
    print("\nOpening Brigador with "+str(len(MODS_SELECTED))+" mods.")

    # Start the Brigador exe
    subprocess.call(["../../../brigador.exe"], cwd=r"../../../")

    # Check if the python should close
    if(not SETTINGS['Settings'].getboolean("remainOpen")):
        exit()

# Populates the selected mods in the settings file
def populateModsFromSettings():
    # Mark global
    global SETTINGS

    # Check if settings was instantiated
    if "Mods" in SETTINGS:
        # Loop through the mods in settings
        for mod in SETTINGS['Mods']:
            MODS_SELECTED.append(mod)
    else:
        # Report problem
        print("The Settings file hasn't been loaded yet, so no data could be fetched.")

# Begin Operation
if __name__ == '__main__':
    main()