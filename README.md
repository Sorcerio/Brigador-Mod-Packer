# Brigador Mod Packer
A tool for packing formatted Brigador Mods into the game written in Python and using the developers provided modding tools.

## Requirments
* [Python Runtime Enviroment](https://www.python.org/downloads/)
* [Brigador Mod Tool](http://stellarjockeys.com/BrigadorModKit.zip)
* `_modkit` File Compatible Mod(s)

## `_modkit` File Compatible Mods
A `_modkit` File Compatible Mod is a mod that has been developed with a link structure that allows it to be inside the Brigador `_modkit` file and correctly link to it's accompanying assets.
If you are unsure if your mod is a `_modkit` File Compatible Mod, ask the person who developed the mod or ask on the [Brigador Discord Channel](https://discord.gg/z4Egp3A) where you can find more content for Brigador!

## Where to Download Mods
* [Brigador Discord Channel](https://discord.gg/z4Egp3A)
* [Brigador Mod Requisition](http://brodymcmedia.com/mediaContent/Tools/BrigadorModSpot/)
* [Brigador Modding Reddit](https://www.reddit.com/r/BrigadorModding/)

## How to Use
1. Unpack your Brigador game files using the [Brigador Mod Tool](http://stellarjockeys.com/BrigadorModKit.zip).
2. Ensure you have a version of the [Python Runtime Enviroment](https://www.python.org/downloads/) installed on your computer.
3. Download or Clone this repo.
4. Place download/clone in your `_modkit` folder located at `INSTALL_DIRECTORY/Brigador Up-Armored Edition/assets/_modkit`.
5. Run the `BrigadorModPacker.py` file in Python IDLE or your favorite command line console with `python BrigadorModPacker.py` in the packer's directory.
6. Choose to manually or automatically repack your Brigador files.
7. Start the game with your new mods.