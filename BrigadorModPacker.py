# Allows for easy packaging of mod materials into the global.json file
# To use, follow the standard operating precedures detailed in the repo

# Imports
import os
import json

# Main Thread
def main():
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
        gblFile = open(gblDir,"r")
    else:
        print("Could not find global.json. Exiting.")
        exit()

    # Report
    print("Parsing mod files...")

    # Loop through all mod files
    for path in modDirs:
        # Open and load json
        print(path)
        with open(path, "r") as jsonFile:
            try:
                # Parse json data
                data = json.load(jsonFile)
                print(data['archetype'])
            except Exception:
                print(path+" is not a valid .json file")

    # Close global.json
    gblFile.close()

# Begin Operation
if __name__ == '__main__':
    main()
