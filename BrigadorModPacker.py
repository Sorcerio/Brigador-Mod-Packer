# Allows for easy packaging of mod materials into the global.json file
# To use, follow the standard operating precedures detailed in the repo

# Imports
import os
import json

# Config
# Category Name for any vehicle mods to be placed under
CATEGORY_NAME = "VARIOUS | SNC Requisistions"

# Globals
GLOBAL_JSON = {}

# Main Thread
def main():
    # Globals
    global GLOBAL_JSON

    # Print welcome
    print("[ BRIGADOR MOD PACKER ]")

    # Alert User
    print("\nCounting Mod Files...")

    # Count Mods
    modDirs = []
    for dirpath, dirnames, filenames in os.walk("../"):
        # Ignore the mod packer folder
        if "BrigadorModPacker" not in dirpath:
            # Loop through all files in directory
            for filename in filenames:
                if filename != "global.json":
                    # Formulate path
                    path = (dirpath+"/"+filename).replace("\\", "/").replace("//", "/")

                    # Only select json files
                    if os.fsdecode(filename).endswith(".json"):
                        # Add to mod file directory list
                        modDirs.append(path)

    # Report
    print(str(len(modDirs))+" mod files found")
    print("\nLocating global.json...")

    # Find global.json
    gblDir = "../../data/global.json"
    if os.path.isfile(gblDir):
        print("global.json found")
        gblFile = open(gblDir,"r",encoding="latin-1")
        GLOBAL_JSON = json.load(gblFile, encoding="latin-1")
    else:
        print("Could not find global.json. Exiting.")
        exit()

    # Report
    print("\nParsing and adding mod files...")

    # Loop through all mod files
    for path in modDirs:
        # Open and load json
        with open(path, "r") as jsonFile:
            try:
                # Parse json data
                data = json.load(jsonFile)
            except Exception:
                print(path+" is not a valid .json file")
            else:
                # Add mod to global
                addModToGlobal(data, path)

    # Report
    print("Finished adding mod files")
    print("\nSaving global.json...")

    # Close Global
    gblFile.close()

    # Open global.json as write
    gblWriteFile = open(gblDir,"w")

    # Write to file
    json.dump(GLOBAL_JSON,gblWriteFile)

    # Close global.json
    gblWriteFile.close()

    # Report
    print("global.json has been saved")

# Adds the given json mod to global
# Currently Supports: All Vehicles, All Weapons, Pilots, Specials
def addModToGlobal(data, path):
    try:
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

        elif data['archetype'] == "PILOT":
            # Append to Pilots
            GLOBAL_JSON['pilots'].append(pathToStandard(path))

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

        elif "MISSION" in data['archetype']:
            # Append to Missions
            GLOBAL_JSON['missions'].append(pathToStandard(path))

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
