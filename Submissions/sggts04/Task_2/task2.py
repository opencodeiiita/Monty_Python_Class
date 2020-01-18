import os
import shutil

os.chdir(os.getcwd() + "\\My_Files\\")

for filename in os.listdir():
    if os.path.isfile(filename):
        ext = filename.split('.')[1]
        extFolder = ext.upper()
        if not os.path.exists(extFolder):
            os.mkdir(extFolder)
        shutil.move(filename, extFolder)