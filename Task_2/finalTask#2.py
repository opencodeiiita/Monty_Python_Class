import shutil
import os

s = '..\\...\\Monty_Python_Class\\Task_2\\My_Files\\'

for folders, subfolders ,files in os.walk(s):
    for file in files:
        name, ext = os.path.splitext(file)
        if os.path.exists(os.path.join(s,(ext.upper())[1:])):
            shutil.move(os.path.join(s,file), os.path.join(s,(ext.upper())[1:]))
        else:
            os.mkdir(os.path.join(s,(ext.upper())[1:]))
            shutil.move(os.path.join(s,file), os.path.join(s,(ext.upper())[1:]))
