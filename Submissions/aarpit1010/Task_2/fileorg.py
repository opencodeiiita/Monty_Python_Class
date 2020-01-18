import os
import shutil

rootpath="../../../Task_2/My_Files"
os.chdir(rootpath)

for filename in os.listdir():
    if os.path.isfile(filename):
        name = filename.split('.')[1]
        folder=name.upper()
        if not os.path.exists(folder):
            os.mkdir(folder)
        shutil.move(filename,folder)
