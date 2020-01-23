import os
import shutil

os.chdir("../../../Task_2/My_Files")
for filename in os.listdir():
    if os.path.isfile(filename):
        folder = filename.split(".")[1].upper()
        try:
            os.mkdir(folder)
            shutil.move(filename,folder)
        except:
            shutil.move(filename,folder)
