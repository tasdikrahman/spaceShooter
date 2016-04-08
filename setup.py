import sys
from cx_Freeze import setup, Executable
import os

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "pygame"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

pygame_py_file = os.path.join('spaceshooter', 'spaceShooter.py')

## The image and sound files are added manually into the zip file
## A fix for this would be released

setup(  name = "Space Shooter",
        version = "0.0.2",
        description = "classic retro game made using pygame",
        options = {"build_exe": build_exe_options},
        executables = [Executable(pygame_py_file, base=base)]
)