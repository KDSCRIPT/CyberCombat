import sys
import setuptools
from cx_Freeze import Executable
from cx_Freeze import setup
import sys

import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"],
                     "include_files": [
                                       ]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {
    'build_exe': {
        'include_files': [
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
        ],
    },
}

setup(name="Cyber Combat",
      version="1.0.2",
      description="2D SHOOTING GAME",
      options={"build_exe": build_exe_options},
      executables=[Executable(script="main-exe.py",
                              base=base,
                              icon="icons\cc.ico")])