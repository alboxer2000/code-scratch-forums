import sys
import os
import tkinter
from tkinter.filedialog import askdirectory
from tkinter.simpledialog import askstring
path = sys.executable
try:
    path = path.replace('pythonw.exe',"")
except:
    pass
try:
    path = path.replace('python3.exe',"")
except:
    pass
try:
    path = path.replace('python.exe',"")
except:
    pass
PYTHON_PATH = path
PYTHON = str(PYTHON_PATH + "python3.exe")
directory = askdirectory(title="Open Project", mustexist=True, initialdir=".")
filename = askstring("Project Name", "Write the project name here:")
print(f"cd {directory}")
print(f"{PYTHON} {filename}.py")
os.system("cmd")
