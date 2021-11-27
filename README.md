# Fusion360-Write-UserInterface
This is a far more in-depth and advanced version of "Write user interface to a file API Sample" from https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-d2b85a7e-fd08-11e4-9e07-3417ebd3d5be

Quick warning, if you choose to have the full indepth file created, prepare for a file containing about 30,000 lines of text :) this script literally parses the entire fusion ui in a second or two including all controls, tabs, panels, workspaces, and command definitions so every command fusion has is included along with important information such as its index in whatever parent ui item and its visibility or if it is native to fusion. You want the fusion ui in a file? well you can have it lol. Use a good text editor that lets you hide groups. VS code click anywhere in the file then hit ctrl+k+0 and it will collapse all groups. You can also import the script as if it were a python library and do stuff with it since it is designed to be a sort of python-y nested class.

See the "UiObjects.py" file in this folder for my current ui layout and to see what the output of the full in-depth option looks like
