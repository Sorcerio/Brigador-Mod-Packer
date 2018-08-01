# Allows for easy packaging of mod materials into the global.json file
# To use, follow the standard operating precedures detailed in the repo

# Imports
import os

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
                path = (dirpath+"/"+filename).replace("\\","/").replace("//","/")

                # Only select json files
                if os.fsdecode(filename).endswith(".json"):
                    # Add to mod file directory list
                    modDirs.append(path)

    # Report on count
    print(str(len(modDirs))+" mod files found")
    print(modDirs)

# Begin Operation
if __name__ == '__main__':
    main()
