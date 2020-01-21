import shutil
import os

 
for folders, subfolders ,files in os.walk("..\\...\\Monty_Python_Class\\Task_2\\My_Files\\'):
    for file in files:
        name, ext = os.path.splitext(file)
        if os.path.exists('..\\...\\Monty_Python_Class\\Task_2\\My_Files\\'+ (ext.upper())[1:]):
            shutil.move('..\\...\\Monty_Python_Class\\Task_2\\My_Files\\'+str(file), '..\\...\\Monty_Python_Class\\Task_2\\My_Files\\'+(ext.upper())[1:])
        else:
            os.mkdir('..\\...\\Monty_Python_Class\\Task_2\\My_Files\\'+(ext.upper())[1:])
            shutil.move('..\\...\\Monty_Python_Class\\Task_2\\My_Files\\'+str(file), '..\\...\\Monty_Python_Class\\Task_2\\My_Files\\'+(ext.upper())[1:])




