import shutil
import os
import os.path
os.chdir('My_Files')
for abc in os.listdir():
    if os.path.isfile(abc):
        extension_of_file=abc.split('.')[1]
        folder_to_extract=extension_of_file.upper()
        if os.path.exists(folder_to_extract):
            shutil.move(abc, folder_to_extract)
        elif not os.path.exists(folder_to_extract):
            os.mkdir(folder_to_extract)
            shutil.move(abc, folder_to_extract)
