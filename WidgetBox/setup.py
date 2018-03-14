import sys
from cx_Freeze import setup, Executable
import os


os.environ['TCL_LIBRARY'] = r'D:\ProgramData\anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\ProgramData\anaconda3\tcl\tk8.6'


# Dependencies are automatically detected, but it might need
# fine tuning. 'D:/ProgramData/anaconda3/DLLs/tcl86t.dll', 'D:/ProgramData/anaconda3/DLLs/tk86t.dll',
buildOptions = dict(
    packages = [],
    excludes = [],
    include_files=['./icons']
)


base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('WidgetBox.py', base=base,icon="./icons/Widget_Box.ico")
]

setup(name='WidgetBox',
      version = '2.71828',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)