import os,shutil
os.chdir("../../../Task_2/My_Files")
for filename in os.listdir():
    if os.path.isfile(filename):
        ext = filename.split(".")[1]
        try:
            os.mkdir(ext)
            shutil.move(filename,ext)
        except:
            shutil.move(filename,ext)