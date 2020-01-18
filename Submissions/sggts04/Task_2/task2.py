import os
import shutil

os.chdir("../../../Task_2/My_Files")    #change current folder

for filename in os.listdir():
    if os.path.isfile(filename):
        ext = filename.split('.')[1]
        extFolder = ext.upper()
        if not os.path.exists(extFolder):
            os.mkdir(extFolder)
        shutil.move(filename, extFolder)