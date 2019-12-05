# Brigador Mod Packer
A tool for packing formatted Brigador Mods into the game.

Currently All Vehicles, All Weapons, Pilots, Specials, Maps, and all linked files are supported in the system.

## Requirments
* [Python 3](https://www.python.org/downloads/)
* [Official Brigador Mod Tools](http://stellarjockeys.com/BrigadorModKit.zip)

## Installation
1. Install a clean version of Brigador.
    * It's important that the first time you run the Brigador Mod Packer that your `global.json` file is Vanilla.
1. Install [Python 3](https://www.python.org/downloads/) if you do not already have it.
1. Install the [Official Brigador Mod Tools](http://stellarjockeys.com/BrigadorModKit.zip) to your Brigador installation.
1. Run the `dumppack.bat` file that is now in your Brigador installation from the Official Brigador Mod Tools.
    * The `dumppack.bat` process will take a minute or two.
1. Download a _Release_ from this repo and place it in your new `assets/_modkit/` folder.
    * Should result in a path similar to `INSTALL_DIRECTORY/Brigador Up-Armored Edition/assets/_modkit/Brigador-Mod-Packer/`.
1. Install any mods you wish to use by adding thier top level folder to your `assets/_modkit/` folder.
    * Ex: `assets/_modkit/YOUR_MOD/` where `YOUR_MOD` is the file containing items like extra folders, `modDetails.json`, and `.json` files.
    * See the `Where to Download Mods` section for more info on where to find mods.
1. Run the `ModPacker.py` file in your `Brigador-Mod-Packer/` folder.
    * If you do not know how to run a Python script, please consult this [article on the topic](https://realpython.com/run-python-scripts/#how-to-run-python-scripts-using-the-command-line).
1. Select the mods you wish to use from the `Select Mods` menu on the Brigador Mod Packer's main menu.
1. Once mods are selected, confirm and select `Play with Selected Mods` from the Brigador Mod Packer's main menu.
    * The mods you have selected will then be compiled (if needed) and, once complete (which may take a minute or two), Brigador will launch.

## Where to Download Mods
The [Brigador Discord Channel](https://discord.gg/z4Egp3A) is currently the primary place for downloading mods.

## For the Modders
### The modDetails.json File
The `modDetails.json` file is a data file that the Brigador Mod Packer can interact with that provides more information to both the user and the mod packer itself when handling your mod. While any mod _without_ a `modDetails.json` file (refered to here as a Legacy Mod), will still work within the Brigador Mod Packer your mod will miss out on some benefits.

### Benefits of the modDetails.json File
The benefits of including a `modDetails.json` file include:
* A custom title for your mod within in the mod selection menu.
* A custom description for your mod within the mod selection menu.
* The inclusion of the author's (your) name/alias in the mod selection menu.
* A custom vehicle category for your mod within Brigador.
* You can specify which files should be loaded by the Mod Packer and which should not.
* You can specify if an included file (like a Vehicle or a Weapon) should be avalible to the player.
* Your mod won't be listed a Legacy Mod in the Mod Selection menu.

### Creating Your Own  modDetails.json File
Luckily, making a `modDetails.json` file is easy. As such a template file been included in this repository. Additionaly, by adding your mod to the `assets/_modkit/` folder and going to `Utilities > Generate a Mod Details file` in the Brigador Mod Packer you can go through a guided process to create one. Once the file is created, it can loaded into any text editor and modified further.

### The modDetails.json File's Attributes
* `title`: The title that your mod should be displayed with in the Mod Selection Menu.
* `description`: The description that your mod should be displayed with in the Mod Selection Menu.
* `author`: The author that your mod should be displayed with in the Mod Selection Menu.
* `version`: The author that your mod should be displayed with in the Mod Selection Menu. Standard format is `v1.0.0`.
* `category`: The category that any Vehicles in your mod should be listed under in game. Standard format is `YOUR_MODS_NAME | SNC Requisitions` to fit the style of the Vanilla categories, but can be almost anything.
* `files`: A list of the files that should be included when compiling your mod into Brigador.
    * `path`: The path (starting with `assets/_modkit/`) that Brigador can find your `.json` file at.
    * `forPlayer`: A boolean stating if the player should be able to equip the accompanying `path`'s contents from the in game Requisitions menu. `True` would indicate the player can purchase and equip the item.

Do not include `"` in any of these fields unless it is escaped as such `\"`.
