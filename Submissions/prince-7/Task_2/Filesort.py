import shutil
import os
import os.path
os.chdir('../../../Task_2/My_Files')
for filename in os.listdir():
    if os.path.isfile(filename):
        extensions=filename.split('.')[1]
        folder_to_extract= extensions.upper()
        if os.path.exists(folder_to_extract):
            shutil.move(filename, folder_to_extract)
        elif not os.path.exists(folder_to_extract):
            os.mkdir(folder_to_extract)
            shutil.move(filename, folder_to_extract)