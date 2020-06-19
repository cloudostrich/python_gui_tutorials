import cx_Freeze
import sys
import matplotlib

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [cx_Freeze.Executable("tkintervid28.py", base=base, icon='clienticon.ico')]

cx_Freeze.setup(
    name = "Seaofbtc-client",
    options = {"build_exe": {"packages":["tkinter", "matplotlib"], "include_files":["clienticon.ico"]}},
    version = "0.01",
    description = "Sea of BTC trading app",
    executables = executables)

'''
open holding folder in a cmd window.
>>python setup.py build

>> python setup.py bdist.msi  # 64 bit installer
'''
