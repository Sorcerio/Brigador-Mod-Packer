# Brigador Mod Packer
A tool for packing formatted Brigador Mods into the game written in Python and using the developers provided modding tools.

## Requirments
* [Python 3](https://www.python.org/downloads/)
* [Brigador Mod Tool](http://stellarjockeys.com/BrigadorModKit.zip)
* `_modkit File` Compatible Mod(s)

## `_modkit` File Compatible Mods
A `_modkit File` Compatible Mod is a mod that has been developed with a link structure that allows it to be inside the Brigador `_modkit file` and correctly link to it's accompanying assets.
If you are unsure if your mod is a `_modkit File` Compatible Mod, ask the person who developed the mod or ask on the [Brigador Discord Channel](https://discord.gg/z4Egp3A) where you can find more content for Brigador!

Currently All Vehicles, All Weapons, Pilots, and Specials are supported in the system.

## Where to Download Mods
* [Brigador Discord Channel](https://discord.gg/z4Egp3A)
* [Brigador Mod Requisition](http://brodymcmedia.com/mediaContent/Tools/BrigadorModSpot/)
* [Brigador Modding Reddit](https://www.reddit.com/r/BrigadorModding/)

## How to Use
1. Unpack your Brigador game files using the [Brigador Mod Tool](http://stellarjockeys.com/BrigadorModKit.zip) by following its instructions.
1. Ensure you have a [Python 3](https://www.python.org/downloads/) installed on your computer.
1. Download a _Release_ from this repo to your `_modkit` folder.
    * Will result in a path similar to `INSTALL_DIRECTORY/Brigador Up-Armored Edition/assets/_modkit/BrigadorModPacker/`.
1. Run the `ModPacker.py` file in Python IDLE or your favorite command line console with `python BrigadorModPacker.py` in the packer's directory.
1. Use the `Select Mods` menu to select what mods you would like to initialize.
1. Once your mods are setup, simply use `Play with Selected Mods` or, to play Vanilla, `Play without Mods` to start Brigador in the selected configuration.
