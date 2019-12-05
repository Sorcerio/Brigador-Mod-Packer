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
