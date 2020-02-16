import os
import shutil

path='My_Files/'

sortfiles = os.listdir(path)

for files in sortfiles :
    name, extension = os.path.splitext(files)

    extension = extension[1:]

   

    if os.path.exists(path + '/' + extension):
        shutil.move(path + '/' + files , path + '/' + extension + '/' + files)

    else :
        os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + files , path + '/' + extension + '/' + files) 
